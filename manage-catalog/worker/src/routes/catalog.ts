import { Hono } from "hono";
import { getClient, query } from "../db";
import type {
  Env,
  DisplayProfileRow,
  CurriculumCollectionRow,
  CurriculumSeriesRow,
  CollectionWithItems,
  SeriesWithItems,
  CurriculumSummary,
} from "../types";

const catalog = new Hono<{ Bindings: Env }>();

/**
 * GET /catalog/:profileId
 *
 * Returns the full catalog view for a given display profile.
 * Applies display_order_override on top of base display_order values.
 * Filters out items with effective display_order < 0.
 * Sorts by effective display_order descending.
 */
catalog.get("/:profileId", async (c) => {
  const profileId = parseInt(c.req.param("profileId"));
  if (isNaN(profileId)) {
    return c.json({ error: "Invalid profileId" }, 400);
  }

  const client = await getClient(c.env);
  try {
    // Fetch the display profile
    const profiles = await query<DisplayProfileRow>(
      client,
      `SELECT * FROM display_profile WHERE id = $1`,
      [profileId]
    );
    if (profiles.length === 0) {
      return c.json({ error: "Display profile not found" }, 404);
    }

    const profile = profiles[0];
    const overrides = profile.display_order_override;
    const collectionOverrides = overrides.collections ?? {};
    const seriesOverrides = overrides.series ?? {};
    const curriculumOverrides = overrides.curriculums ?? {};

    // Fetch all collections
    const allCollections = await query<CurriculumCollectionRow>(
      client,
      `SELECT id, title, description, is_public, thumbnail, display_order, created_at
       FROM curriculum_collections`
    );

    // Compute effective display_order for collections and filter visible ones
    const visibleCollections = allCollections
      .map((col) => ({
        ...col,
        effective_display_order: collectionOverrides[col.id] ?? col.display_order,
      }))
      .filter((col) => col.effective_display_order >= 0)
      .sort((a, b) => b.effective_display_order - a.effective_display_order);

    if (visibleCollections.length === 0) {
      return c.json({ profile_id: profileId, description: profile.description, collections: [] });
    }

    const collectionIds = visibleCollections.map((col) => col.id);

    // Fetch series linked to visible collections
    const collectionSeriesLinks = await query<{
      curriculum_collection_id: string;
      curriculum_series_id: string;
    }>(
      client,
      `SELECT curriculum_collection_id, curriculum_series_id
       FROM curriculum_collection_series
       WHERE curriculum_collection_id = ANY($1)`,
      [collectionIds]
    );

    const seriesIds = [...new Set(collectionSeriesLinks.map((l) => l.curriculum_series_id))];

    let seriesMap = new Map<string, CurriculumSeriesRow>();
    if (seriesIds.length > 0) {
      const seriesRows = await query<CurriculumSeriesRow>(
        client,
        `SELECT id, title, description, thumbnail, is_public, display_order, created_at
         FROM curriculum_series WHERE id = ANY($1)`,
        [seriesIds]
      );
      for (const s of seriesRows) {
        seriesMap.set(s.id, s);
      }
    }

    // Fetch curriculums linked to series
    let seriesCurriculumLinks: { curriculum_series_id: string; curriculum_id: string }[] = [];
    if (seriesIds.length > 0) {
      seriesCurriculumLinks = await query<{
        curriculum_series_id: string;
        curriculum_id: string;
      }>(
        client,
        `SELECT curriculum_series_id, curriculum_id
         FROM curriculum_series_items
         WHERE curriculum_series_id = ANY($1)`,
        [seriesIds]
      );
    }

    // Fetch curriculums linked directly to collections
    const collectionCurriculumLinks = await query<{
      curriculum_collection_id: string;
      curriculum_id: string;
    }>(
      client,
      `SELECT curriculum_collection_id, curriculum_id
       FROM curriculum_collection_items
       WHERE curriculum_collection_id = ANY($1)`,
      [collectionIds]
    );

    // Gather all curriculum IDs we need
    const allCurriculumIds = [
      ...new Set([
        ...seriesCurriculumLinks.map((l) => l.curriculum_id),
        ...collectionCurriculumLinks.map((l) => l.curriculum_id),
      ]),
    ];

    let curriculumMap = new Map<string, CurriculumSummary>();
    if (allCurriculumIds.length > 0) {
      const curriculumRows = await query<{
        id: string;
        uid: string;
        language: string;
        user_language: string;
        is_public: boolean;
        price: number;
        list_price: number | null;
        display_order: number;
        is_disabled: boolean | null;
      }>(
        client,
        `SELECT id, uid, language, user_language, is_public, price, list_price, display_order, is_disabled
         FROM curriculum WHERE id = ANY($1)`,
        [allCurriculumIds]
      );
      for (const cur of curriculumRows) {
        const effectiveOrder = curriculumOverrides[cur.id] ?? cur.display_order;
        curriculumMap.set(cur.id, {
          ...cur,
          effective_display_order: effectiveOrder,
        });
      }
    }

    // Build the response
    const result: CollectionWithItems[] = visibleCollections.map((col) => {
      // Series for this collection
      const colSeriesIds = collectionSeriesLinks
        .filter((l) => l.curriculum_collection_id === col.id)
        .map((l) => l.curriculum_series_id);

      const seriesItems: SeriesWithItems[] = colSeriesIds
        .map((sid) => {
          const s = seriesMap.get(sid);
          if (!s) return null;
          const effectiveOrder = seriesOverrides[sid] ?? s.display_order;

          // Curriculums in this series
          const seriesCurIds = seriesCurriculumLinks
            .filter((l) => l.curriculum_series_id === sid)
            .map((l) => l.curriculum_id);

          const curItems = seriesCurIds
            .map((cid) => curriculumMap.get(cid))
            .filter((c): c is CurriculumSummary => c != null && c.effective_display_order >= 0)
            .sort((a, b) => b.effective_display_order - a.effective_display_order);

          return {
            ...s,
            effective_display_order: effectiveOrder,
            curriculums: curItems,
          } as SeriesWithItems;
        })
        .filter((s): s is SeriesWithItems => s != null && s.effective_display_order >= 0)
        .sort((a, b) => b.effective_display_order - a.effective_display_order);

      // Direct curriculums for this collection
      const colCurIds = collectionCurriculumLinks
        .filter((l) => l.curriculum_collection_id === col.id)
        .map((l) => l.curriculum_id);

      const directCurriculums = colCurIds
        .map((cid) => curriculumMap.get(cid))
        .filter((c): c is CurriculumSummary => c != null && c.effective_display_order >= 0)
        .sort((a, b) => b.effective_display_order - a.effective_display_order);

      return {
        ...col,
        series: seriesItems,
        curriculums: directCurriculums,
      };
    });

    return c.json({
      profile_id: profileId,
      description: profile.description,
      collections: result,
    });
  } finally {
    await client.end();
  }
});

export default catalog;
