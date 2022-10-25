# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Python, Big data, Machine Learning y Cloud Computing"
copyright = "2022, Santiago Arboleda"
author = "Santiago Arboleda"
release = "0.1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["myst_parser", "sphinx.ext.duration", "nbsphinx"]

templates_path = ["_templates"]
exclude_patterns = []
nbsphinx_allow_errors = True
language = "es"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

import sphinx_rtd_theme

# import furo

html_theme = "sphinx_rtd_theme"
# html_theme = "classic"
html_static_path = ["_static"]
