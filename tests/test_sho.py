#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `sho` package."""

import sys
import unittest
from io import StringIO

import sho

class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio    # free up some memory
        sys.stdout = self._stdout



class TestSho(unittest.TestCase):
    """Tests for Sho package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_simple_import(self):
        """Sample pytest test function with the pytest fixture as an argument."""
        example_string = "test_dd"
        with Capturing() as output:
            sho.w(example_string)
        assert output[0] == example_string
