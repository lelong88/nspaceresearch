export interface Env {
  HYPERDRIVE: Hyperdrive;
}

// Database row types

export interface CurriculumCollectionRow {
  id: string;
  title: string;
  description: string | null;
  is_public: boolean;
  thumbnail: string | null;
  display_order: number;
  created_at: string;
}

export interface CurriculumSeriesRow {
  id: string;
  title: string;
  description: string | null;
  thumbnail: string | null;
  is_public: boolean;
  display_order: number;
  created_at: string;
}

export interface CurriculumRow {
  id: string;
  uid: string;
  language: string;
  user_language: string;
  content: unknown;
  instruction: string | null;
  is_public: boolean;
  price: number;
  list_price: number | null;
  display_order: number;
  is_disabled: boolean | null;
  created_at: string;
}

export interface DisplayProfileRow {
  id: number;
  description: string;
  display_order_override: DisplayOrderOverride;
  created_at: string;
}

export interface DisplayOrderOverride {
  collections?: Record<string, number>;
  series?: Record<string, number>;
  curriculums?: Record<string, number>;
}

// API response types

export interface CollectionWithItems extends CurriculumCollectionRow {
  effective_display_order: number;
  series: SeriesWithItems[];
  curriculums: CurriculumSummary[];
}

export interface SeriesWithItems extends CurriculumSeriesRow {
  effective_display_order: number;
  curriculums: CurriculumSummary[];
}

export interface CurriculumSummary {
  id: string;
  uid: string;
  language: string;
  user_language: string;
  is_public: boolean;
  price: number;
  list_price: number | null;
  display_order: number;
  effective_display_order: number;
  is_disabled: boolean | null;
  title?: string;
  description?: string;
}
