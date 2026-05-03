# Requirements Document

## Introduction

Comprehensive improvement of all 9 display profile `display_order_override` values in the curriculum catalog system. This addresses missing new collections from profile overrides, empty curriculum overrides, and lack of meaningful differentiation in display ordering across audience-specific profiles. All profiles except profile 8 include all content (visible at >= 0); only profile 8 hides adult content with negative values.

## Glossary

- **Display_Profile**: A database entity that defines a personalized catalog view for a target audience by overriding default display_order values
- **Display_Order_Override**: A JSONB field containing override maps for collections, series, and curriculums
- **Collection**: A top-level content grouping in the curriculum hierarchy (default display_order: -2000, hidden unless explicitly overridden to positive)
- **Series**: A sequence of related curriculums within a collection
- **Curriculum**: An individual learning unit containing lessons
- **Catalog_API**: The REST API at `https://catalogapi.step.is` used to update display profiles via PUT requests
- **Hidden_Value**: A negative display_order value (< 0) that hides an item from a catalog view; the standard value is `-1`
- **Visible_Value**: A non-negative display_order value (>= 0) that makes a collection visible in a catalog view
- **French_Collections**: The 5 new French-language collections (ad49khvn, uzs1jq8x, bu0fz4rr, vxuvod0y, 4ke7s1i7)
- **Kids_Multi_Language_Collections**: New kids collections for German (ugnufdje), French (ls4gufq0, gjtcifmu), and Chinese (vd22jc0b)

## Requirements

### Requirement 1: Add French Collections to Relevant Profiles

**User Story:** As a catalog administrator, I want the 5 new French collections included in appropriate display profiles, so that French-language content is discoverable by all relevant audiences.

#### Acceptance Criteria

1. WHEN a Display_Profile targets a general audience (profiles 3, 4, 5, 6, 7), THE Catalog_API SHALL add the French_Collections with positive Visible_Value at a tier consistent with other multi-language collections in that profile
2. WHEN a Display_Profile targets university students (profiles 1, 2), THE Catalog_API SHALL add the French_Collections with positive Visible_Value at a mid-tier position below the primary promoted content
3. WHEN a Display_Profile targets children only (profile 8), THE Catalog_API SHALL add the French_Collections with Hidden_Value of -1 since they are adult content
4. WHEN a Display_Profile targets kids + beginner mix (profile 9), THE Catalog_API SHALL add the French_Collections with positive Visible_Value at a lower tier below kids content
5. THE Display_Profile update SHALL assign differentiated display_order values to French_Collections based on their relevance to each profile's audience (e.g., Business & Career higher for office professionals, Academic & Science higher for academics)

### Requirement 2: Add Multi-Language Kids Collections to Kids Profiles

**User Story:** As a catalog administrator, I want the new German, French, and Chinese kids collections included in profiles 8 and 9, so that children learning multiple languages can discover age-appropriate content.

#### Acceptance Criteria

1. WHEN the Display_Profile with id=8 (Children Age 6-10) is updated, THE Catalog_API SHALL add collections ugnufdje (German kids), ls4gufq0 (French kids), gjtcifmu (French kids), and vd22jc0b (Chinese kids) with positive Visible_Value below the existing Vietnamese kids collections
2. WHEN the Display_Profile with id=9 (Kids + Beginner Mix) is updated, THE Catalog_API SHALL add collections ugnufdje, ls4gufq0, gjtcifmu, and vd22jc0b with positive Visible_Value positioned between the Vietnamese kids collections and the general beginner content
3. THE Kids_Multi_Language_Collections SHALL be ordered with display_order values that reflect a logical language grouping (e.g., French together, then German, then Chinese)

### Requirement 3: Populate Profile 6 Curriculum Overrides

**User Story:** As a catalog administrator, I want profile 6 (Intermediate - Young students) to have meaningful curriculum overrides, so that Fiction and Curious Minds curriculums are promoted for this audience.

#### Acceptance Criteria

1. WHEN the Display_Profile with id=6 has empty curriculum overrides, THE Catalog_API SHALL add curriculum overrides that promote Fiction-related curriculums with higher display_order values
2. WHEN the Display_Profile with id=6 has empty curriculum overrides, THE Catalog_API SHALL add curriculum overrides that promote Curious Minds series curriculums with higher display_order values
3. THE curriculum overrides for profile 6 SHALL use differentiated values (not all the same number) to create a meaningful ordering within the promoted content

### Requirement 4: Differentiate Flat Collection Display Orders

**User Story:** As a catalog administrator, I want collections that currently sit at a flat 1200 to have differentiated display_order values per audience, so that each profile presents a meaningfully curated ordering rather than an arbitrary flat list.

#### Acceptance Criteria

1. WHEN a Display_Profile has multiple collections at the same display_order value of 1200, THE Catalog_API SHALL update those collections to use differentiated values that reflect the audience's priorities
2. WHILE updating flat display_order values, THE Catalog_API SHALL assign higher values to collections more relevant to the profile's target audience and lower values to less relevant collections
3. THE differentiated values SHALL maintain the overall tier structure (promoted content > mid-tier > deprioritized) without disrupting the relative position of explicitly promoted or demoted collections
4. WHEN differentiating values for profile 1 (Medical students), THE Catalog_API SHALL assign higher values to health-related, science, and academic collections within the mid-tier
5. WHEN differentiating values for profile 2 (Economics students), THE Catalog_API SHALL assign higher values to business, finance, and economics-related collections within the mid-tier
6. WHEN differentiating values for profiles 3 and 5 (Office Professionals), THE Catalog_API SHALL assign higher values to professional skills, communication, and business collections within the mid-tier
7. WHEN differentiating values for profile 4 (Beginner Friendly), THE Catalog_API SHALL assign higher values to vocabulary, daily life, and accessible topic collections within the mid-tier
8. WHEN differentiating values for profile 6 (Young students), THE Catalog_API SHALL assign higher values to fiction, stories, culture, and intellectually stimulating collections within the mid-tier
9. WHEN differentiating values for profile 7 (Academics), THE Catalog_API SHALL assign higher values to science, research, philosophy, and academic collections within the mid-tier

### Requirement 5: Tailor Series Overrides Per Audience

**User Story:** As a catalog administrator, I want series overrides to be more tailored per audience, so that within-collection ordering reflects each profile's specific interests.

#### Acceptance Criteria

1. WHEN the Display_Profile with id=1 (Medical students) is updated, THE Catalog_API SHALL promote the Health & Wellness series (e24f29c4) to a higher position relative to other series in that profile
2. WHEN the Display_Profile with id=2 (Economics students) is updated, THE Catalog_API SHALL promote business-related series (The Boardroom 9gfei23g, How the World Really Works 09o7ke5d) to higher positions
3. WHEN the Display_Profile with id=6 (Young students) is updated, THE Catalog_API SHALL promote intellectually stimulating series (Curious Minds db5930f6, Mind & Society kxxkeo1f, The Science Shelf xwznpgdr) to higher positions
4. THE series override updates SHALL preserve the existing series that are already correctly positioned and only adjust relative ordering where improvement is needed

### Requirement 6: Execute Updates Via API

**User Story:** As a catalog administrator, I want all display_order_override changes applied via the Catalog_API PUT endpoint, so that changes are persisted correctly in the database.

#### Acceptance Criteria

1. THE Catalog_API SHALL receive PUT requests to `https://catalogapi.step.is/display-profiles/:id` with body `{display_order_override: {...}}` for each profile update
2. WHEN updating a Display_Profile, THE Catalog_API request body SHALL contain the complete display_order_override object (collections, series, and curriculums sections) since PUT replaces the entire field
3. IF a PUT request to the Catalog_API fails, THEN THE update process SHALL report the failure with the profile id and HTTP status code
4. WHEN all 9 profiles have been updated, THE update process SHALL verify each profile by querying the display_profile_collections view to confirm the changes took effect
