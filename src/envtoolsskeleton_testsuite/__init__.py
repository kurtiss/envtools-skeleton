#!/usr/bin/env python
# encoding: utf-8
"""
__init__.py

Created by Kurtiss Hare on 2011-03-10.
All copyright interest in this code is dedicated to the public domain.
"""

import unittest2 as unittest
from envtoolsskeleton_testsuite.all import cases


def load_tests(loader, tests, pattern):
    suite = unittest.TestSuite()
    for case in cases:
        suite.addTests(loader.loadTestsFromTestCase(case))
    return suite