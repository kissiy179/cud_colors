#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from setuptools import setup
from glob import glob

package_name = os.path.basename(os.path.dirname(__file__))

setup(
    name=package_name,
    version='0.1.0',
    py_modules=[splitext(basename(path))[0] for path in glob('*.py')],
    include_package_data=True,
    python_requires=">=2.7",
    install_requires=[
    ]
)
