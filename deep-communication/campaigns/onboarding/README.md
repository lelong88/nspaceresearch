# Campaign: Onboarding (In-App Banner Series)

- **Type**: evergreen / automated
- **Lang**: en, vi
- **Channel**: in-app banners only (no email)
- **Status**: draft

---

## Concept

A series of **10 contextual in-app banners** that guide new users through the onboarding funnel — from first app open to first learning session. Each banner is tailored to the user's current status and displayed language, nudging them toward the next meaningful action.

Unlike a one-size-fits-all welcome message, this campaign meets users exactly where they are in the journey and speaks to what they need to do next.

---

## Targeting

- **Assigned to**: `zs5AMpVfqkcfDf8CJ9qrXdH58d73` (test user — will change to `all` once validated)
- **Languages**: `en` and `vi` (one banner per status per language = 10 banners total)
- **Link destination**: `https://step.is` (placeholder — will be updated with deep links later)

---

## Banner Matrix

| # | `required_user_status` | Banner type | Purpose |
|---|------------------------|-------------|---------|
| 1 | `not_logged_in` (en) | `standard` | Encourage sign-up — explain that logging in unlocks purchases and learning |
| 2 | `not_logged_in` (vi) | `standard` | Same as above, Vietnamese |
| 3 | `no_credits` (en) | `standard` | Point users to free "0 credit" curriculums, or the wallet icon for referral codes |
| 4 | `no_credits` (vi) | `standard` | Same as above, Vietnamese |
| 5 | `no_purchase_yet` (en) | `standard` | Nudge users to spend their credits on a curriculum to start learning |
| 6 | `no_purchase_yet` (vi) | `standard` | Same as above, Vietnamese |
| 7 | `not_started_yet` (en) | `standard` | Prompt users to tap "Get started" on a purchased curriculum |
| 8 | `not_started_yet` (vi) | `standard` | Same as above, Vietnamese |
| 9 | `started_no_activity_yet` (en) | `minimal` | Congratulate the user for starting; explain the distraction-free philosophy |
| 10 | `started_no_activity_yet` (vi) | `minimal` | Same as above, Vietnamese |

---

## User Status Descriptions

| Status | What it means | What the user needs to do |
|--------|---------------|---------------------------|
| `not_logged_in` | User can browse the catalog but can't purchase or learn | Sign in / create an account |
| `no_credits` | User is logged in but has zero credits | Unlock free "0 credit" curriculums, or tap the wallet icon to enter/share a referral code |
| `no_purchase_yet` | User has credits but hasn't unlocked any curriculum | Use credits to unlock a curriculum |
| `not_started_yet` | User purchased ≥1 curriculum but hasn't tapped "Get started" | Tap "Get started" on any owned curriculum |
| `started_no_activity_yet` | User just started a curriculum (likely seeing the distraction-free page) | Congratulate them; explain the distraction-free design and encourage first activity |

---

## Banner Type Rationale

- **`standard`** for statuses 1–8: these users are on the catalog page (browsing, not yet committed). Standard banners appear there.
- **`minimal`** for statuses 9–10: these users have committed to a curriculum and are on the distraction-free page. Minimal banners respect that focused context.

---

## Implementation Notes

- All banners are created via `POST /api/banners` with `required_user_status` and `required_user_language` set on the banner definition
- Assigned to test user via `POST /api/banners/:id/assign` with `user_uid = 'zs5AMpVfqkcfDf8CJ9qrXdH58d73'`
- Once validated, switch assignments to `user_uid = 'all'` for global delivery
- Link URLs (`https://step.is`) are placeholders — update with appropriate deep links before going live

---

## Next Steps

1. Write banner copy (title + subtitle) for each of the 10 banners
2. Create banners via the API and assign to test user
3. Validate rendering and targeting logic in the app
4. Update link destinations with proper deep links
5. Switch to `user_uid = 'all'` for production rollout
