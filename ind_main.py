"""
Created on May 4, 2021

@author: poojan.kothari
"""

from util import common_utils
from util import constants

print(constants.banner)

pin_code = common_utils.get_pin_code()
date = common_utils.get_date()
rec_factor = common_utils.get_recurrence_factor()
window_type = common_utils.get_window_type()

common_utils.invoke_vaccine_tracker(
    window_type,
    pin_code,
    date,
    rec_factor)

print("Done")

