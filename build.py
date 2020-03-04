#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import shutil
import subprocess
import os.path
import zipfile
import platform
import os.path
from distutils.dir_util import copy_tree

def call(cmd):
    print(cmd)
    p = subprocess.Popen(cmd, shell=True)
    ret = p.wait()

class CurrentDir:
	def __init__(self, path):
		self.prev = os.getcwd()
		self.path = path
	def __enter__(self):
		os.chdir(self.path)
		print("cd: " + os.getcwd())
		return self
	def __exit__(self, type, value, traceback):
		os.chdir(self.prev)
		print("cd: " + os.getcwd())

if not os.path.exists("_Lumino"):
    #call("git clone --depth 1 -b v0.9.0 https://github.com/LuminoEngine/Lumino.git _Lumino")
    call("git clone https://github.com/LuminoEngine/Lumino.git _Lumino")
    
with CurrentDir('_Lumino/docs/Doxygen'):
    call("build_doc.bat")

print("copy _Lumino/docs/Doxygen/html to _site/api/reference-cpp")
copy_tree("_Lumino/docs/Doxygen/html", "_site/api/reference-cpp")

with CurrentDir('_Lumino/tools/Bindings/Ruby/APIReference'):
    call("yardoc *.rb")

print("copy _Lumino/tools/Bindings/Ruby/APIReference/doc to _site/api/reference-ruby")
copy_tree("_Lumino/tools/Bindings/Ruby/APIReference/doc", "_site/api/reference-ruby")

call("docfx build")
