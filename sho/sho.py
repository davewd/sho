# -*- coding: utf-8 -*-
from sho.constants import OUTPUT_TYPE
# db.py
import sys
import pandas as pd
import tempfile
from pivottablejs import pivot_ui
import webbrowser

# this is a pointer to the module object instance itself.
this = sys.modules[__name__]

def display_as_string_via_html(obj):
    """
    Display a variable as a defaulty HTML
        :param obj: the object to be displayed.
    """


def display_string_output(obj):
    """
    Display a string
        :param obj: 
    """
    print(obj)

def display_dataframe_with_pivotablejs(obj):
    """
    Function to convert a variable to a pivotable js
        :param obj: table object to display,
    """
    tf = tempfile.NamedTemporaryFile(delete=False, prefix="sho_", suffix=".html")
    file_path = tf.name
    cols = list(obj.columns.values)
    pivot_ui(obj, outfile_path=file_path, cols=cols)
    browser= webbrowser.get('chrome')
    browser.open(file_path)

def display_html_output(obj):
    """
    Function to convert a variable to a pivotable js
        :param obj: table object to display,
    """
    if type(obj) == pd.core.frame.DataFrame :
        display_dataframe_with_pivotablejs(obj)
        # Create more elif's here !
    else:
        display_as_string_via_html(obj)

def get_output_type_for_object(obj):
    """
    If Default selected allow the community to decide the best way to show your variable for you !
        :param obj: variable to display
    """
    return OUTPUT_TYPE.HTML.value

def output( obj, output_type):
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


"""Main module."""
def w(obj, output_type=OUTPUT_TYPE.DEFAULT.value):
    """
    Main function called, defaults to 
        :param obj: the variable to show
        :param output_type=OUTPUT_TYPE.DEFAULT.value: ability to force output types under certain scenarios
    """
    output(obj,output_type);