import os
import sys
sys.path.insert(0, os.path.abspath('..'))

project = 'TheApix'
author = 'Vivekkumar-IN'
release = '1.2.7'
copyright = "2024-present, Vivek"

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
exclude_patterns = []
html_title = "TheApix"

html_theme = "furo"
html_copy_source = False
html_static_path = ['_static']
html_css_files = [
    "css/custom.css",
]

html_theme_options = {
    "navigation_with_keys": True,
}