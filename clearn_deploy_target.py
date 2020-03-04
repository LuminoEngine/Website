#!/usr/bin/env python
# -*- coding: utf-8 -*-

import shutil
import os

print("clearn _docs_repo...")

def safe_rmtree(path):
    if os.path.isdir(path):
        shutil.rmtree(path)

def safe_rmfile(path):
    if os.path.isfile(path):
        os.remove(path)

safe_rmtree("_docs_repo/api")
safe_rmtree("_docs_repo/articles")
safe_rmtree("_docs_repo/fonts")
safe_rmtree("_docs_repo/img")
safe_rmtree("_docs_repo/styles")
safe_rmfile("_docs_repo/logo.svg")
safe_rmfile("_docs_repo/manifest.json")
safe_rmfile("_docs_repo/Readme.html")
safe_rmfile("_docs_repo/search-stopwords.json")
safe_rmfile("_docs_repo/toc.html")
safe_rmfile("_docs_repo/xrefmap.yml")
safe_rmfile("_docs_repo/favicon.ico")
safe_rmfile("_docs_repo/index.html")
safe_rmfile("_docs_repo/logo.png")
