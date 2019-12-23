from sho.sho import output
from sho.constants import OUTPUT_TYPES

"""Main module."""
def w(obj, output_type=OUTPUT_TYPE.DEFAULT.value):
    """
    Main function called, defaults to 
        :param obj: the variable to show
        :param output_type=OUTPUT_TYPE.DEFAULT.value: ability to force output types under certain scenarios
    """
    output(obj,output_type);