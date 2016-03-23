# -*- coding:utf-8 -*
from distutils.core import setup
import py2exe


setup(
    zipfile=None,
    windows=[{"script": "cvs2xml.py","icon_resources": [(1, "client.ico")]}],
    version = "1.0.0", 
    description = "xls to xml", 
)