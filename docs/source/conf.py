import os
import re
import sys
import inspect
import logging
import datetime


sys.path.insert(0, os.path.abspath("../.."))

import TheApi


logging.basicConfig(level=logging.INFO)
log = logging.info

log("\n\n\n\n\n\n\n\n\n\n\n")

project = "TheApix"
author = "VivekKumar-IN"
version = TheApi.__version__
copyright = f"{datetime.date.today().year}, {author}"

autosummary_generate = True

extensions = [
    "sphinx.ext.autosummary",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_copybutton",
]

templates_path = ["_templates"]
exclude_patterns = []

docs = os.getcwd()

for root, _, files in os.walk(docs):
    for file in files:
        if file.endswith(".rst"):
            file_path = os.path.join(root, file)
            with open(file_path, "r") as f:
                content = f.read()

            cls_to_replace = re.findall(r"\{(\w+)_methods\}", content)
            for cla in cls_to_replace:
                cls = getattr(TheApi, cla)
                methods = inspect.getmembers(cls, predicate=inspect.isfunction)
                method_list = "\n   ".join(
                    [f"{cla}.{name}" for name, _ in methods if not name.startswith("_")]
                )
                content = content.replace(f"{{{cla}_methods}}", method_list)

            toctrees = re.findall(r"\{(\w+)_toctree\}", content)
            for cla in toctrees:
                cls = getattr(TheApi, cla)
                methods = inspect.getmembers(cls, predicate=inspect.isfunction)
                method_list = "\n   ".join(
                    [name for name, _ in methods if not name.startswith("_")]
                )
                content = content.replace(f"{{{cla}_toctree}}", method_list)

                for method_name, _ in methods:
                    if not method_name.startswith("_"):
                        rst_file_name = os.path.join(root, f"{method_name}.rst")
                        with open(rst_file_name, "w") as method_file:
                            method_file.write(
                                f"{method_name}\n{'=' * len(method_name)}\n\n"
                                f".. currentmodule:: TheApi\n\n"
                                f".. automethod:: {cla}.{method_name}\n"
                            )
                        log(f"Generated file: {rst_file_name}")

            with open(file_path, "w") as f:
                f.write(content)

log("\n\n\n\n\n\n\n\n\n\n\n")
