# Statistical Programming and Reproducible Data Science Reader Companion

Felix Larry Essilfie, PhD

[Open the reader site](https://felixlarry7.github.io/statistical-programming-companion/) · [Download the complete reader ZIP](https://zenodo.org/records/24382209/files/Statistical_Programming_Stage8_Reader_Companion.zip?download=1) · [View the archived release on Zenodo](https://zenodo.org/records/24382209)

This companion serves the ebook, paperback and hardcover editions. Find executable code for Python, R, Stata and SQL, teaching datasets, reference outputs, reproducibility guides, 892 chapter exercises, 80 selected worked answers and twelve applied projects. Open the data catalogue for source attribution and instructions for obtaining controlled data from its custodian.

## Use the downloads

Extract the complete Zenodo ZIP, or download `Reader_Companion_1.zip` and `Reader_Companion_2.zip` and extract both into the same folder. Each route gives the same 2,033 files and the SHA-256 manifest. See [reader use and attribution](READER_USE.md).

From the extracted `Statistical_Programming_Reader_Companion` folder, check the files and rebuild the project reports.

```sh
sha256sum -c --quiet MANIFEST.sha256
python projects/build.py --output build/project-reports
```

The [Stage 8 version DOI](https://doi.org/10.5281/zenodo.24382209) identifies this archive. The [all-versions DOI](https://doi.org/10.5281/zenodo.24382208) follows the latest release.

## Rebuild the site

Run `quarto render`. Copy the six HTML pages in `_render` to the repository root alongside their QMD sources, indexes, two ZIP volumes and `.nojekyll`. GitHub Pages serves the root of `main`. The HTML pages embed their display dependencies.

To combine the mirror volumes into one ZIP, run the following from the repository root. It checks both volume hashes and every manifest entry. A recompressed ZIP can have a different container checksum while containing identical files.

```sh
python combine_reader.py . reconstructed_reader_companion.zip
```
