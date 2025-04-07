import datetime
import logging
import os
import sys

sys.path.insert(0, os.path.abspath("../.."))

import TheApi

logging.basicConfig(level=logging.INFO)

log = logging.info

log("\n\n\n\n\n\n\n\n\n\n\n")

project = "TheApix"
author = "VivekKumar-IN"
release = TheApi.__version__
version = ".".join(release.split(".")[:2])
copyright = f"{datetime.date.today().year}, {author}"

autosummary_generate = True

extensions = [
    "sphinx.ext.autosummary",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_copybutton",
    "sphinx_exec_code",
]


templates_path = ["_templates"]
exclude_patterns = []

html_title = f"TheApix v{version}"
# html_theme = "sphinx_rtd_theme"
html_theme = "furo"
html_copy_source = False
html_show_copyright = False
html_static_path = ["_static"]
html_extra_path = ["_templates"]
html_css_files = ["css/pyrogram.css"]
html_favicon = html_static_path[0] + "/img/TheApix.ico"
html_show_sphinx = False
html_theme_options = {
    "navigation_with_keys": True,
    "footer_icons": [
        {
            # Telegram channel logo
            "name": "Telegram Channel",
            "url": "https://t.me/TheTeamVivek",
            "html": (
                '<svg stroke="currentColor" fill="#0088cc" stroke-width="0" '
                'viewBox="0 0 16 16" style="width: 2em; height: 2em;" '
                'xmlns="http://www.w3.org/2000/svg">'
                '<path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM8.287 5.906c-.778.324-2.334.994'
                "-4.666 2.01-.378.15-.577.298-.595.442-.03.243.275.339.69.47l.175.055c.408.133."
                "958.288 1.243.294.26.006.549-.1.868-.32 2.179-1.471 3.304-2.214 3.374-2.23.0"
                "5-.012.12-.026.166.016.047.041.042.12.037.141-.03.129-1.227 1.241-1.846 1.81"
                "7-.193.18-.33.307-.358.336a8.154 8.154 0 0 1-.188.186c-.38.366-.664.64.015 1.08"
                "8.327.216.589.393.85.571.284.194.568.387.936.629.093.06.183.125.27.187.331.23"
                "6.63.448.997.414.214-.02.435-.22.547-.82.265-1.417.786-4.486.906-5.751a1.426 "
                "1.426 0 0 0-.013-.315.337.337 0 0 0-.114-.217.526.526 0 0 0-.31-.093c-.3.005-.7"
                '63.166-2.984 1.09z"></path></svg>'
            ),
            "class": "",
        },
        {  # Github logo
            "name": "GitHub",
            "url": "https://github.com/Vivekkumar-IN/TheApi",
            "html": (
                '<svg stroke="currentColor" fill="currentColor" stroke-width="0" '
                'viewBox="0 0 16 16" style="width: 2em; height: 2em;">'
                '<path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 '
                "2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.4"
                "9-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23"
                ".82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 "
                "0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.2"
                "7 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.5"
                "1.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 "
                '1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z">'
                "</path></svg>"
            ),
            "class": "",
        },
    ],
}
pygments_style = "default"
# pygments_dark_style = "native"

napoleon_include_special_with_doc = False
napoleon_use_rtype = False
napoleon_use_param = True
