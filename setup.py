#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from setuptools import setup
from glob import glob

dir_path = os.path.dirname(__file__)
package_name = os.path.basename(dir_path)
module_names = [splitext(basename(path))[0] for path in glob('{}/python/*.py'.format(dir_path))]

setup(
    name=package_name,
    version='0.1.0',
    py_modules=module_names,
    include_package_data=True,
    python_requires=">=2.7",
    install_requires=[
    ]
)
