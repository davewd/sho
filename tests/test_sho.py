#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `sho` package."""

import pytest
import unittest

from sho import sho
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

import sys

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

    def test_simple_import():
        """Sample pytest test function with the pytest fixture as an argument."""
        import sho
        example_string = "test_dd"
        with Capturing() as output:
            sho.w(example_string)
        assert output == example_string

