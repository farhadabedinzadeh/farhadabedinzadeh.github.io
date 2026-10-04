# Updating the academic website

The site remains a GitHub Pages-compatible Jekyll project. The portfolio pages use
`_layouts/academic.html`, with dependency-free styling and JavaScript.

- Homepage: `_pages/about.html`
- Complete publications page: `_pages/publications.html`
- Online CV: `_pages/cv.html`
- Publication metadata and selected-paper flags: `_data/publications.yml`
- Author, contact and SEO settings: `_config.yml`
- Navigation: `_data/navigation.yml`
- Styling: `assets/css/academic.css`
- Publication filters: `assets/js/academic.js`

The original theme remains available for other layouts. Only the new portfolio
layout is loaded on these pages, so it does not load the original jQuery,
slideshow or citation-counter scripts. Image originals remain in the repository;
the portfolio uses smaller WebP derivatives under `images/optimized/`.
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
