# Implementation Plan: Display Profile Improvements

## Overview

Apply improved `display_order_override` JSON payloads to all 9 display profiles via PUT requests to the Catalog API. Each task reads the current state, computes the new payload incorporating French collections, kids collections, differentiated values, series tailoring, and curriculum overrides as specified in the design, then sends the PUT and verifies the result.

No code changes are involved — this is purely data operations against the existing API.

## Tasks

- [ ] 1. Update Profile 1 (Medical students)
  - [x] 1.1 Read current display_order_override for profile 1
    - GET `https://catalogapi.step.is/display-profiles/1`
    - Record the full current `display_order_override` object (collections, series, curriculums)
    - _Requirements: 6.2_

  - [x] 1.2 Compute new display_order_override for profile 1
    - Add French collections with medical-priority ordering: ad49khvn: 1188, uzs1jq8x: 1185, bu0fz4rr: 1183, vxuvod0y: 1182, 4ke7s1i7: 1186
    - Differentiate existing flat 1200 values into audience-specific rankings (health, science, academic collections higher)
    - Promote Health & Wellness series (e24f29c4) to a higher position
    - Preserve all existing overrides not being modified
    - _Requirements: 1.2, 1.5, 4.1, 4.4, 5.1, 5.4_

  - [x] 1.3 Send PUT request for profile 1
    - PUT `https://catalogapi.step.is/display-profiles/1` with body `{display_order_override: <computed payload>}`
    - Confirm 2xx response
    - _Requirements: 6.1, 6.2_

  - [x] 1.4 Verify profile 1 update
    - Query `display_profile_collections` view for profile_id=1
    - Confirm French collections appear with expected display_order values
    - Confirm no previously-visible collections were accidentally hidden
    - Confirm differentiated ordering reflects medical audience priorities
    - _Requirements: 6.4_

- [ ] 2. Update Profile 2 (Economics students)
  - [x] 2.1 Read current display_order_override for profile 2
    - GET `https://catalogapi.step.is/display-profiles/2`
    - Record the full current `display_order_override` object
    - _Requirements: 6.2_

  - [x] 2.2 Compute new display_order_override for profile 2
    - Add French collections with economics-priority ordering: uzs1jq8x: 1188, ad49khvn: 1185, bu0fz4rr: 1183, vxuvod0y: 1182, 4ke7s1i7: 1184
    - Differentiate existing flat 1200 values (business, finance, economics collections higher)
    - Promote business series (The Boardroom 9gfei23g, How the World Really Works 09o7ke5d) to higher positions
    - Preserve all existing overrides not being modified
    - _Requirements: 1.2, 1.5, 4.1, 4.5, 5.2, 5.4_

  - [x] 2.3 Send PUT request for profile 2
    - PUT `https://catalogapi.step.is/display-profiles/2` with body `{display_order_override: <computed payload>}`
    - Confirm 2xx response
    - _Requirements: 6.1, 6.2_

  - [x] 2.4 Verify profile 2 update
    - Query `display_profile_collections` view for profile_id=2
    - Confirm French collections appear with expected display_order values
    - Confirm differentiated ordering reflects economics audience priorities
    - _Requirements: 6.4_

- [ ] 3. Update Profile 3 (Office Pro Beginner)
  - [x] 3.1 Read current display_order_override for profile 3
    - GET `https://catalogapi.step.is/display-profiles/3`
    - Record the full current `display_order_override` object
    - _Requirements: 6.2_

  - [x] 3.2 Compute new display_order_override for profile 3
    - Add French collections with office-priority ordering: uzs1jq8x: 1188, bu0fz4rr: 1185, vxuvod0y: 1184, ad49khvn: 1183, 4ke7s1i7: 1182
    - Differentiate existing flat 1200 values (professional skills, communication, business collections higher)
    - Preserve all existing overrides not being modified
    - _Requirements: 1.1, 1.5, 4.1, 4.6_

  - [x] 3.3 Send PUT request for profile 3
    - PUT `https://catalogapi.step.is/display-profiles/3` with body `{display_order_override: <computed payload>}`
    - Confirm 2xx response
    - _Requirements: 6.1, 6.2_

  - [x] 3.4 Verify profile 3 update
    - Query `display_profile_collections` view for profile_id=3
    - Confirm French collections appear with expected display_order values
    - Confirm differentiated ordering reflects office professional priorities
    - _Requirements: 6.4_

- [ ] 4. Update Profile 4 (Beginner Friendly)
  - [x] 4.1 Read current display_order_override for profile 4
    - GET `https://catalogapi.step.is/display-profiles/4`
    - Record the full current `display_order_override` object
    - _Requirements: 6.2_

  - [x] 4.2 Compute new display_order_override for profile 4
    - Add French collections with beginner-priority ordering: vxuvod0y: 1188, bu0fz4rr: 1186, uzs1jq8x: 1184, ad49khvn: 1182, 4ke7s1i7: 1183
    - Differentiate existing flat 1200 values (vocabulary, daily life, accessible topic collections higher)
    - Preserve all existing overrides not being modified
    - _Requirements: 1.1, 1.5, 4.1, 4.7_

  - [x] 4.3 Send PUT request for profile 4
    - PUT `https://catalogapi.step.is/display-profiles/4` with body `{display_order_override: <computed payload>}`
    - Confirm 2xx response
    - _Requirements: 6.1, 6.2_

  - [x] 4.4 Verify profile 4 update
    - Query `display_profile_collections` view for profile_id=4
    - Confirm French collections appear with expected display_order values
    - Confirm differentiated ordering reflects beginner audience priorities
    - _Requirements: 6.4_

- [x] 5. Checkpoint — Verify first 4 profiles
  - Ensure all updates for profiles 1–4 are verified, ask the user if questions arise.

- [ ] 6. Update Profile 5 (Office Pro Intermediate+)
  - [x] 6.1 Read current display_order_override for profile 5
    - GET `https://catalogapi.step.is/display-profiles/5`
    - Record the full current `display_order_override` object
    - _Requirements: 6.2_

  - [x] 6.2 Compute new display_order_override for profile 5
    - Add French collections with office-priority ordering (same as profile 3): uzs1jq8x: 1188, bu0fz4rr: 1185, vxuvod0y: 1184, ad49khvn: 1183, 4ke7s1i7: 1182
    - Differentiate existing flat 1200 values (professional skills, communication, business collections higher)
    - Preserve all existing overrides not being modified
    - _Requirements: 1.1, 1.5, 4.1, 4.6_

  - [x] 6.3 Send PUT request for profile 5
    - PUT `https://catalogapi.step.is/display-profiles/5` with body `{display_order_override: <computed payload>}`
    - Confirm 2xx response
    - _Requirements: 6.1, 6.2_

  - [x] 6.4 Verify profile 5 update
    - Query `display_profile_collections` view for profile_id=5
    - Confirm French collections appear with expected display_order values
    - Confirm differentiated ordering reflects office professional priorities
    - _Requirements: 6.4_

- [ ] 7. Update Profile 6 (Young students)
  - [x] 7.1 Read current display_order_override for profile 6
    - GET `https://catalogapi.step.is/display-profiles/6`
    - Record the full current `display_order_override` object
    - _Requirements: 6.2_

  - [x] 7.2 Compute new display_order_override for profile 6
    - Add French collections with young-student-priority ordering: bu0fz4rr: 1188, 4ke7s1i7: 1186, ad49khvn: 1185, vxuvod0y: 1184, uzs1jq8x: 1183
    - Differentiate existing flat 1200 values (fiction, stories, culture, intellectually stimulating collections higher)
    - Promote series: Curious Minds (db5930f6), Mind & Society (kxxkeo1f), The Science Shelf (xwznpgdr) to higher positions
    - Add curriculum overrides promoting Fiction curriculums (1300–1350 range) and Curious Minds curriculums (1250–1300 range) with differentiated values
    - Preserve all existing overrides not being modified
    - _Requirements: 1.1, 1.5, 3.1, 3.2, 3.3, 4.1, 4.8, 5.3, 5.4_

  - [x] 7.3 Send PUT request for profile 6
    - PUT `https://catalogapi.step.is/display-profiles/6` with body `{display_order_override: <computed payload>}`
    - Confirm 2xx response
    - _Requirements: 6.1, 6.2_

  - [x] 7.4 Verify profile 6 update
    - Query `display_profile_collections` view for profile_id=6
    - Confirm French collections appear with expected display_order values
    - Confirm curriculum overrides are populated and differentiated
    - Confirm series overrides reflect young student priorities
    - _Requirements: 6.4_

- [ ] 8. Update Profile 7 (Academics)
  - [x] 8.1 Read current display_order_override for profile 7
    - GET `https://catalogapi.step.is/display-profiles/7`
    - Record the full current `display_order_override` object
    - _Requirements: 6.2_

  - [x] 8.2 Compute new display_order_override for profile 7
    - Add French collections with academic-priority ordering: ad49khvn: 1189, 4ke7s1i7: 1187, bu0fz4rr: 1185, uzs1jq8x: 1184, vxuvod0y: 1183
    - Differentiate existing flat 1200 values (science, research, philosophy, academic collections higher)
    - Preserve all existing overrides not being modified
    - _Requirements: 1.1, 1.5, 4.1, 4.9_

  - [x] 8.3 Send PUT request for profile 7
    - PUT `https://catalogapi.step.is/display-profiles/7` with body `{display_order_override: <computed payload>}`
    - Confirm 2xx response
    - _Requirements: 6.1, 6.2_

  - [x] 8.4 Verify profile 7 update
    - Query `display_profile_collections` view for profile_id=7
    - Confirm French collections appear with expected display_order values
    - Confirm differentiated ordering reflects academic audience priorities
    - _Requirements: 6.4_

- [x] 9. Checkpoint — Verify profiles 5–7
  - Ensure all updates for profiles 5–7 are verified, ask the user if questions arise.

- [ ] 10. Update Profile 8 (Children 6-10)
  - [x] 10.1 Read current display_order_override for profile 8
    - GET `https://catalogapi.step.is/display-profiles/8`
    - Record the full current `display_order_override` object
    - _Requirements: 6.2_

  - [x] 10.2 Compute new display_order_override for profile 8
    - Add kids multi-language collections with values below existing Vietnamese kids: ls4gufq0: 1185, gjtcifmu: 1184, ugnufdje: 1183, vd22jc0b: 1182
    - Add French collections as hidden (all set to -1): ad49khvn: -1, uzs1jq8x: -1, bu0fz4rr: -1, vxuvod0y: -1, 4ke7s1i7: -1
    - Preserve all existing overrides not being modified
    - _Requirements: 1.3, 2.1, 2.3_

  - [x] 10.3 Send PUT request for profile 8
    - PUT `https://catalogapi.step.is/display-profiles/8` with body `{display_order_override: <computed payload>}`
    - Confirm 2xx response
    - _Requirements: 6.1, 6.2_

  - [x] 10.4 Verify profile 8 update
    - Query `display_profile_collections` view for profile_id=8
    - Confirm kids multi-language collections appear with correct positive display_order values
    - Confirm French collections are hidden (display_order < 0)
    - Confirm no previously-visible kids content was accidentally hidden
    - _Requirements: 6.4_

- [ ] 11. Update Profile 9 (Kids + Beginner Mix)
  - [x] 11.1 Read current display_order_override for profile 9
    - GET `https://catalogapi.step.is/display-profiles/9`
    - Record the full current `display_order_override` object
    - _Requirements: 6.2_

  - [x] 11.2 Compute new display_order_override for profile 9
    - Add kids multi-language collections between Vietnamese kids and beginner content: ls4gufq0: 1192, gjtcifmu: 1191, ugnufdje: 1190, vd22jc0b: 1189
    - Add French collections at lower tier: vxuvod0y: 1170, bu0fz4rr: 1168, uzs1jq8x: 1166, ad49khvn: 1164, 4ke7s1i7: 1165
    - Preserve all existing overrides not being modified
    - _Requirements: 1.4, 1.5, 2.2, 2.3_

  - [x] 11.3 Send PUT request for profile 9
    - PUT `https://catalogapi.step.is/display-profiles/9` with body `{display_order_override: <computed payload>}`
    - Confirm 2xx response
    - _Requirements: 6.1, 6.2_

  - [x] 11.4 Verify profile 9 update
    - Query `display_profile_collections` view for profile_id=9
    - Confirm kids multi-language collections appear between Vietnamese kids and beginner content
    - Confirm French collections appear at lower tier with correct values
    - _Requirements: 6.4_

- [x] 12. Final checkpoint — Verify all 9 profiles
  - Ensure all 9 profiles have been updated and verified successfully, ask the user if questions arise.
  - Optionally spot-check via GET `/catalog/:profileId` for a few profiles to confirm the resolved catalog view reflects changes.

## Notes

- This is a data-only implementation — no code files are created or modified
- Each task uses the existing PUT endpoint; the full `display_order_override` object must be sent (PUT replaces the entire field)
- Always read current state before computing the new payload to avoid accidentally removing existing overrides
- The `display_profile_collections` view is the primary verification mechanism
- If any PUT returns a non-2xx status, stop and investigate before proceeding
