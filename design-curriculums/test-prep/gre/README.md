# GRE Verbal Mastery

- Series ID: `1r0l5nos`
- Language: en-en, Level: advanced
- Public: yes
- Collection: Exam Prep (`72d8f528`)

## Curriculums (8 total, 10 vocab words each = 80 words)

| # | ID | Title | Vocab |
|---|---|---|---|
| 1 | Cmr9eU0N9iKmsab9 | The Paradox of Altruism | Altruism, Benevolent, Magnanimity, Philanthropy, Ameliorate, Egregious, Perfunctory, Ostensible, Duplicity, Venal |
| 2 | hbIsZ5ybO2WUIVXM | The Architecture of Dissent | Dissent, Subversive, Hegemony, Iconoclast, Polemical, Acquiesce, Capitulate, Intransigent, Recalcitrant, Placate |
| 3 | VaWBmLdwRAmCNCgZ | The Erosion of Certainty | Epistemology, Empirical, Dogmatic, Axiomatic, Conjecture, Equivocate, Obfuscate, Specious, Fallacious, Tenuous |
| 4 | vLLGUMe8G2jAPPBi | The Calculus of Risk | Stochastic, Volatility, Contingent, Mitigate, Prudent, Precipitous, Exacerbate, Untenable, Commensurate, Exigent |
| 5 | 68zwn6VrXQhJI2bD | The Rhetoric of Science | Paradigm, Anomaly, Corroborate, Hypothesis, Replicable, Spurious, Pedantic, Didactic, Esoteric, Arcane |
| 6 | K0LgDeOCbpX6MPIQ | The Geography of Inequality | Stratification, Disparity, Endemic, Systemic, Entrenched, Ameliorate, Palliative, Pernicious, Insidious, Intractable |
| 7 | WNZm9J7FSxXc0aTZ | The Ethics of Memory | Mnemonic, Ephemeral, Indelible, Nostalgia, Elegy, Revisionist, Expunge, Vindicate, Exonerate, Culpable |
| 8 | BuUXrnuaTxXI0wmS | The Limits of Language | Lexicon, Vernacular, Eloquent, Articulate, Nuance, Ambiguous, Euphemism, Taciturn, Loquacious, Verbose |

## Find in DB
```sql
SELECT * FROM curriculum_series WHERE id = '1r0l5nos';
SELECT c.id, c.content->>'title' as title, c.display_order, cat.overall_level
FROM curriculum_series_items csi
JOIN curriculum c ON c.id = csi.curriculum_id
LEFT JOIN curriculum_all_tags cat ON c.id = cat.id
WHERE csi.curriculum_series_id = '1r0l5nos'
ORDER BY c.display_order;
```

## How it was created
Same 4-session pattern as GMAT and TOEIC (5 words S1, 5 words S2, review S3, full article + farewell S4). Reading passages use dense, analytical GRE-style prose — philosophical arguments, academic debates, interdisciplinary essays. Each curriculum created via a separate hand-crafted script (`create_gre_1_altruism.py` through `create_gre_8_language.py`, deleted after import). Series created via `create_gre_series.py` (also deleted). All content individually written — no templates or string interpolation. Full content recoverable via `curriculum/getOne` or MCP postgres.
