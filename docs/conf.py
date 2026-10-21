# Configuration file for the Sphinx documentation builder.
# https://www.sphinx-doc.org/en/master/usage/configuration.html

project = "yanga-project"
copyright = "2026, Alexandru Maxiniuc"
author = "Alexandru Maxiniuc"

extensions = ["myst_parser"]
myst_enable_extensions = ["colon_fence", "attrs_block"]
source_suffix = [".md"]
exclude_patterns = ["_build", "_theme", "Thumbs.db", ".DS_Store"]

html_theme = "drawing"
html_theme_path = ["_theme"]
html_permalinks = False
html_use_index = False
html_last_updated_fmt = "%Y-%m-%d"
html_context = {
    "drawn": "www.maxiniuc.com",
    # The drawing set, in sheet order. None marks a sheet that is not issued yet.
    "sheets": [
        ("index", "Overview"),
        ("tools", "Tools"),
        (None, "Workflows"),
        (None, "Trainings"),
        (None, "Examples"),
        ("logbook", "Logbook"),
    ],
}
