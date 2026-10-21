# yanga-project.github.io

Source of [yanga-project.dev](https://yanga-project.dev), the website of yanga-project, a software product line engineering platform.

The site is drawn as a technical drawing set: every page is a sheet, and the header is the sheet index.

## Build

```shell
pypeline run
```

This creates the virtual environment and builds the site into `build/docs`. Open `build/docs/index.html` to look at it.

## Add a sheet

1. Write `docs/<name>.md`.
2. Add it to the hidden toctree in `docs/index.md`.
3. Add `("<name>", "<Title>")` to `sheets` in `docs/conf.py`. Entries with `None` are shown as not issued yet.

## Add a logbook entry

Write `docs/logbook/YYYY-MM-DD-<slug>.md` with a `# YYYY-MM-DD · Title` heading. Entries are listed newest first by file name.

## Layout

- `docs/_theme/drawing/` holds the Sphinx theme: `layout.html` draws the frame, the sheet index and the title block, and `static/` holds the stylesheet, logo and font.
- The font is [osifont](https://github.com/hikikomori82/osifont) (LGPL3 with font exception).

## Deployment

Every push to `main` runs `pypeline run` in GitHub Actions and publishes `build/docs` to the `gh-pages` branch, which GitHub Pages serves at yanga-project.dev.
