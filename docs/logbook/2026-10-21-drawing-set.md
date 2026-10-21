# 2026-10-21 · Why the site looks like a technical drawing

A product line is engineered, so the site is drawn like an engineering drawing set. Each page is a sheet with a number, and the header is the sheet index.

## Taken from standards

- The colours are RAL 7035, 7016 and 9016, the greys and white of industrial control cabinets.
- The font is osifont, lettering after ISO 3098.
- Lines come in two widths, thick and thin, as in ISO 128.

## Adding a sheet

A new page is a Markdown file plus one line in `conf.py`:

```python
"sheets": [
    ("index", "Overview"),
    ("tools", "Tools"),
    ("logbook", "Logbook"),
],
```
