# -*- coding: utf-8 -*-
import logging
import os

import sys
import tempfile
import webbrowser
from typing import Any

import pandas as pd

from pivottablejs import pivot_ui
from sho.constants import OUTPUT_TYPE

logger = logging.info(__name__)

# this is a pointer to the module object instance itself.
this = sys.modules[__name__]

def display_as_string_via_html(obj: Any):
    """
    Display a variable as a default HTML
        :param obj: the object to be displayed.
    """


def display_string_output(obj: Any):
    """
    Display a string
        :param obj: 
    """
    print(obj)

def display_dataframe_with_pivotablejs(obj: Any):
    """
    Function to convert a variable to a pivotable js
        :param obj: table object to display,
    """
    tf = tempfile.NamedTemporaryFile(prefix="sho_", suffix=".html", delete=False)
    file_path = tf.name
    cols = list(obj.columns.values)
    print(f"File Name : {tf.name}")
    pivot_ui(obj, outfile_path=file_path, vals=cols)
    browser = webbrowser.get('chrome')
    browser.open('file://' + os.path.realpath(file_path))
    sleep(5)
    logger.info(f"File Name : {tf.name}")

def display_dataframe_with_pandas_profiling(obj: Any):
    """
    Function to convert a variable to a pivotable js
        :param obj: table object to display,
    """
    import pandas_profiling
    tf = tempfile.NamedTemporaryFile(prefix="sho_", suffix=".html")
    file_path = tf.name
    profile = obj.profile_report(title='Pandas Profiling Report')
    profile.to_file(output_file=file_path)  
    browser= webbrowser.get('chrome')
    browser.open('file://' + os.path.realpath(file_path))

def display_html_output(obj: Any):
    """
    Function to convert a variable to a pivotable js
        :param obj: table object to display,
    """
    if type(obj) == pd.core.frame.DataFrame :
        display_dataframe_with_pivotablejs(obj)
        # Create more elif's here !
    else:
        display_as_string_via_html(obj)

def get_output_type_for_object(obj: Any):
    """
    If Default selected allow the community to decide the best way to show your variable for you !
        :param obj: variable to display
    """
    return OUTPUT_TYPE.HTML.value

def output( obj: Any, output_type: str):
    """
    Function to map to desired output type
        :param obj: variable to display
        :param output_type: desired output type
    """
    if output_type == OUTPUT_TYPE.DEFAULT.value :
        output_type = get_output_type_for_object(obj)
    
    switcher = {    OUTPUT_TYPE.HTML.value : this.display_html_output,
                    OUTPUT_TYPE.STRING.value : this.display_string_output}
    switcher[output_type](obj)

def output_detail( obj: Any, output_type: str):
    """
    Function to map to desired output type
        :param obj: variable to display
        :param output_type: desired output type
    """
    if output_type == OUTPUT_TYPE.DEFAULT.value :
        output_type = get_output_type_for_object(obj)
    
    switcher = {    OUTPUT_TYPE.HTML.value : this.display_detailed_html_output,
                    OUTPUT_TYPE.STRING.value : this.display_detailed_string_output}
    switcher[output_type](obj)
