# -*- coding: utf-8 -*-
from sho.constants import OUTPUT_TYPE

def display_with_string(obj):
    """
    Display a string
        :param obj: 
    """

def display_with_pivotablejs(obj):
    """
    Function to convert a variable to a pivotable js
        :param obj: table object to display,
    """

def display_html_ouput(obj):
    """
    Function to convert a variable to a pivotable js
        :param obj: table object to display,
    """
    print("HTML")

def get_output_type_for_object(obj):
    """
    If Default selected allow the community to decide the best way to show your variable for you !
        :param obj: variable to display
    """
    return OUTPUT_TYPE.STRING.value

def output( obj, output_type):
    """
    Function to map to desired output type
        :param obj: variable to display
        :param output_type: desired output type
    """
    if output_type == OUTPUT_TYPE.DEFAULT.value :
        output_type = get_output_type_for_object(obj)
    
    switcher = {OUTPUT_TYPE.HTML.value : display_html_output}
    switcher[output_type](obj)

"""Main module."""
def w(obj, output_type=OUTPUT_TYPE.DEFAULT.value):
    """
    Main function called, defaults to 
        :param obj: the variable to show
        :param output_type=OUTPUT_TYPE.DEFAULT.value: ability to force output types under certain scenarios
    """
    output(obj,output_type);