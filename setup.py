#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from setuptools import setup

package_name = os.path.basename(os.path.dirname(__file__))

setup(
    name=package_name,
    version='0.1.0',
    url='https://github.com/kissiy179/cud_colors',
    py_modules=['cud_colors'],
    include_package_data=True,
    python_requires=">=2.7",
    install_requires=[
    ]
)
