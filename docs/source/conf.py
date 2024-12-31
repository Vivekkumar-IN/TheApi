import os
import sys
import inspect


sys.path.insert(0, os.path.abspath("../.."))

from TheApi import Client, __version__


project = "TheApix"
author = "VivekKumar-IN"
version = __version__
copyright = f"%Y, {author}"
autosummary_generate = True

extensions = [
    "sphinx.ext.autosummary",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    # 'sphinx.ext.viewcode',
]

templates_path = ["_templates"]
exclude_patterns = []

html_title = f"TheApix v{version}"
html_theme = "furo"
html_copy_source = False
html_static_path = ["_static"]
html_css_files = ["css/pyrogram.css"]

html_theme_options = {
    "navigation_with_keys": True,
    "footer_icons": [
        {
            "name": "Telegram Channel",
            "url": "https://t.me/TheTeamVivek",
            "html": (
                '<svg stroke="currentColor" fill="currentColor" stroke-width="0" '
                'viewBox="0 0 16 16" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg">'
                '<path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM8.287 5.906c-.778.324-2.334.994..."></path></svg>'
            ),
            "class": "",
        },
        {
            "name": "GitHub",
            "url": f"https://github.com/Vivekkumar-in/TheApi/tree/dev",
            "html": (
                '<svg stroke="currentColor" fill="currentColor" stroke-width="0" '
                'viewBox="0 0 16 16"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8..."></path></svg>'
            ),
            "class": "",
        },
    ],
}

pygments_style = "default"
pygments_dark_style = "native"

napoleon_include_special_with_doc = False
napoleon_use_rtype = False

client_methods = [
    f"Client.{name}"
    for name, func in inspect.getmembers(Client, predicate=inspect.isfunction)
    if not name.startswith("_")
]


client_methods = "\n    ".join(client_methods)


with open("docs/source/client.rst", "r") as file:
    content = file.read()

content = content.replace("{client_methods}", client_methods_str)

with open("docs/source/client.rst", "w") as file:
    file.write(content)
