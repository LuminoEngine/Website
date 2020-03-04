#!/usr/bin/env python
# -*- coding: utf-8 -*-

import shutil
import os

shutil.rmtree("_docs_repo/api")
shutil.rmtree("_docs_repo/articles")
shutil.rmtree("_docs_repo/fonts")
shutil.rmtree("_docs_repo/img")
shutil.rmtree("_docs_repo/styles")
os.remove("logo.svg")
os.remove("manifest.json")
os.remove("Readme.html")
os.remove("search-stopwords.json")
os.remove("toc.html")
os.remove("xrefmap.yml")
os.remove("favicon.ico")
os.remove("index.html")
os.remove("logo.png")
