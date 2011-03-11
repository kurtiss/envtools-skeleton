#!/usr/bin/env python
# encoding: utf-8
"""
__init__.py

Created by Kurtiss Hare on 2011-03-10.
All copyright interest in this code is dedicated to the public domain.
"""

from setuptools import setup, find_packages
import os

execfile(os.path.join('src', 'envtoolsskeleton', 'version.py'))

setup(
    name = 'envtools-skeleton',
    version = VERSION,
    description = 'envtools-skeleton does good things.',
    author = 'Kurtiss Hare',
    author_email = 'kurtiss@gmail.com',
    url = 'http://www.github.com/kurtiss/envtools-skeleton',
    packages = [p for p in find_packages('src') if re.match('envtoolsskeleton(?:\.|$)', p)],
    package_dir = {'':'src'}
    scripts = [],
    classifiers = [
        # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    ],
    install_requires = [
        # additional dependencies
    ],
    zip_safe = False
)