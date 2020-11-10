#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from os.path import dirname, basename, splitext, exists
from glob import glob
from setuptools import setup

def _requires_from_file(filename):
    if not exists(filename):
        return []
    
    return open(filename).read().splitlines()

dir_path = dirname(__file__)
package_name = basename(dir_path)
module_names = [splitext(basename(path))[0] for path in glob(r'{}\python\*.py'.format(dir_path))]
requires_packages = _requires_from_file(r'{}\requirements.txt'.format(dir_path))

print(package_name)
print(module_names)
print(requires_packages)

setup(
    name='cud_colors',
    version='0.1.0',
    package_dir={"": "python"},
    py_modules=['cud_colors'],
    include_package_data=True,
    zip_safe=False,
    python_requires=">=2.7",
    install_requires=[
    ]
)
