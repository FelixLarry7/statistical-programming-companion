# Reader data routes

The bundled teaching extracts support all twelve project reports. The
data catalogue and field index give grain, keys, regular source IDs and
hashes. The original Stata logs and result exports document licensed
execution. The book source uses matching original Python, R and SQL
programmes. See **verification/evidence/chapter_coverage.csv** for the
supported role in a particular chapter.

## Provider holdings

| Data | What comes with the reader package | Access to original holdings |
| --- | --- | --- |
| World Development Indicators | Scoped analytical CSVs and series attribution | World Bank bulk and API routes in the provider register |
| Bank of Ghana D02 | Calculation summaries, original chart and number-checking outputs | Historical effective-date table and reconstruction command below |
| Ghana census geography and water | Sixteen-region teaching crosswalk, weights and pinned geography with credits | Ghana Statistical Service report and geoBoundaries vintage |
| UCI Online Retail | Attributed recoded teaching extract and rebuild code | UCI dataset archive, D09-01 |
| Penn World Table 11.0 | Selected fields, WDI crosswalk and fitted panel | DataverseNL workbook, D12-01 |
| FAOSTAT D07 | Identifier and flag documentation, original agricultural teaching fixtures | FAOSTAT bulk route in the catalogue |
| Licensed surveys and programme records | Synthetic teaching datasets and documented empirical adaptations | Apply to the original custodian listed in **rights/custodian_access.md** |

Provider archives may change. Match the version, use the documented
checksums and keep any newer download as a distinct dataset. Controlled
microdata remain with their custodian.

## Reproduce the Bank of Ghana context

From the companion root, use the official Bank of Ghana policy history
page and match the frozen analytical CSV before repeating the complete
Part VIII multi-engine run. The reader restore command retrieves the
effective-date table, cuts it at 31 December 2024, and matches the
fingerprint of the generated daily teaching input. The complete
licensed Stata replay then uses the matching original input.

~~~sh
python data/acquisition/restore_policy_reader.py
~~~

To use a previously saved copy of the table page, pass its local HTML path as
`--html`. The public reader archive contains the archived Stata result
and log. The policy restore command fills the required archival input
and assembles the Part VIII replay input for readers. The growth and
index baselines in Project P01 and all twelve worked project reports
are available before this additional step.

## Optional full run

The book runner checks the fingerprints of the 94 catalogue assets.
The original FAO contextual file with source flags uses the provider
route. To repeat the full Stage 6 audit with unchanged file fingerprints,
the separately furnished author-review evidence is needed. The public
reader package contains all of the row and chapter verification registers
and a checksum manifest of its own files. The project report generator
works against that public package.

- [Bank of Ghana policy history](https://www.bog.gov.gh/monetary-policy/%20policy-rate-trends/)
- [World Development Indicators](https://data.worldbank.org/)
- [FAOSTAT Crops and livestock products](https://www.fao.org/faostat/en/#data/QCL)
- [UCI Online Retail](https://doi.org/10.24432/C5BW33)
- [Penn World Table 11.0](https://doi.org/10.34894/FABVLR)
