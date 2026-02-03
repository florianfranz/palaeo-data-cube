# Configuration file for the Sphinx documentation builder.

project = 'Palaeo Data Cube'
copyright = '2026, Florian Franziskakis'
author = 'Florian Franziskakis'
release = '0.1.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']