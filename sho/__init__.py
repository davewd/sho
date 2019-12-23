# -*- coding: utf-8 -*-
from sho.constants import OUTPUT_TYPE
from sho.sho import output

"""Top-level package for sho."""

__author__ = """Dave Dawson"""
__email__ = 'davedawson.co@gmail.com'
__version__ = '0.1.0'

"""Main module."""
def w(obj, output_type=OUTPUT_TYPE.DEFAULT.value):
    """
    Main function called, defaults to 
        :param obj: the variable to show
        :param output_type=OUTPUT_TYPE.DEFAULT.value: ability to force output types under certain scenarios
    """
    output(obj,output_type);