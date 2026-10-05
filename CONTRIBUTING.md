# Updating the academic website

The site remains a GitHub Pages-compatible Jekyll project. The portfolio pages use
`_layouts/academic.html`, with dependency-free styling and JavaScript.

- Homepage: `_pages/about.html`
- Complete publications page: `_pages/publications.html`
- Online CV: `_pages/cv.html`
- Publication metadata, type and selected-paper flags: `_data/publications.yml`
- Topic groups: `_data/research_areas.yml`
- Dated citation fallback: `_data/scholar_snapshot.yml`
- Author, contact and SEO settings: `_config.yml`
- Navigation: `_data/navigation.yml`
- Styling: `assets/css/academic.css`
- Publication filters: `assets/js/academic.js`

The original theme remains available for other layouts. Only the new portfolio
layout is loaded on these pages, so it does not load the original jQuery,
slideshow or citation-counter scripts. Image originals remain in the repository;
the portrait uses a smaller WebP derivative under `images/optimized/`.
Publication lists are text-only, grouped by subject, with journal/conference labels.
The existing Google Analytics and search verification settings are retained.

## Check locally

```sh
bundle install
bundle exec jekyll build --safe
bundle exec jekyll serve
```

Keep publication titles, author order and links grounded in bibliographic sources.
Do not infer publication status or the end dates of appointments. The CV uses
joining dates for older roles where an end date has not been confirmed.

After changing the online CV, build the site, then run `python scripts/generate_cv.py`
to regenerate `files/cv/Farhad-Abedinzadeh-CV.pdf` from the built CV page. The script
requires `beautifulsoup4` and `reportlab` in a Python virtual environment. Check
every exported PDF page before committing. The online CV also has A4 print styles.

Run `python scripts/generate_preview.py` after the build and CV export to refresh
`preview/site-preview.html`. That review copy embeds styles, images and the PDF,
and includes navigation between all three pages. The preview and generator
scripts are excluded from the published Jekyll output.

Work on `site-improvements` until the owner has reviewed the preview. A merge to
the Pages source branch publishes the changes.

## Citation refresh

The counter initially shows **274 Google Scholar citations**, fetched directly
from the public profile on 4 October 2026. Its date remains visible. The supplied
17-paper list independently agrees with that total.

The frontend requests `gs_data.json` on the existing `google-scholar-stats` branch.
It accepts only a newer, validated record for `rAgss7MAAAAJ`; the old 2024 data is
ignored. On errors, the dated snapshot stays visible.

`.github/workflows/google_scholar_crawler.yaml` runs the public-profile parser on
relevant pushes and manually, and daily after the workflow is on the default
branch. It uses the existing statistics branch with a normal fast-forward push,
without a Scholar secret, proxy, CAPTCHA solver or external scraping service.
Google Scholar may block automated requests: a blocked response fails the job
without replacing the last successful statistics. GitHub may disable schedules
in inactive public repositories; check Actions if refreshes stop.

For local/offline parser checks:

```sh
python scripts/update_scholar_stats.py --html-file profile.html --output results
```

The script also generates a Shields-compatible `gs_data_shieldsio.json`, but the
site renders the count with native text to match its design.
