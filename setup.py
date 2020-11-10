#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from os.path import dirname, basename, splitext
from glob import glob
from setuptools import setup

dir_path = dirname(__file__)
package_name = basename(dir_path)
module_names = [splitext(basename(path))[0] for path in glob('{}\python\*.py'.format(dir_path))]

setup(
    name=package_name,
    version='0.1.0',
    py_modules=module_names,
    include_package_data=True,
    python_requires=">=2.7",
    install_requires=[
    ]
)
