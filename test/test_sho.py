#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `sho` package."""

import sys
import unittest
from io import StringIO
import webbrowser
#import sho
import logging

logger = logging.info(__name__)


class TestSho(unittest.TestCase):
    """Tests for Sho package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_simple_import(self):
        """Sample pytest test function with the pytest fixture as an argument."""
        example_string = "test_dd"
        #with Capturing() as output:
        #    sho.w(example_string)
        #logger.info(output)
        #assert output[0] == example_string

    @unittest.skip("Webrowser Error")
    def test_dataframe_as_html(self):
        """Ensure a simple dataframe can be rendered with html"""
        import pandas as pd
        import sho
        df = pd.DataFrame([{"a":"b"}])
        sho.w(df)
        #import seaborn as sns
        #iris_df = sns.load_dataset('iris')
        #sho.w(iris_df)


if __name__ == "__main__":
    unittest.main()