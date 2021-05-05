"""
Created on May 4, 2021

@author: poojan.kothari
"""

import datetime

banner = """
===================================================================

            WELCOME TO COWIN HELPER UTILS

This is a simple tracker that helps to find available slot and
if available, provide windows notification for the same.
===================================================================
"""

default_pin_code = "401101"
default_rec_fac = 60
default_date = (datetime.date.today() + datetime.timedelta(days=1)).strftime("%d-%m-%Y")
default_min_age = 18

base_url = "https://cdn-api.co-vin.in/api/"
day_session_by_pin = "v2/appointment/sessions/public/findByPin"
seven_days_session_by_pin = "v2/appointment/sessions/public/calendarByPin"

pin_code_regex = r"^[0-9]{6}$"
date_regex = r"^(([0]?[1-9])|([1-2][0-9])|(3[01]))[-](([0]?[1-9])|([1]?[1-2]))[-](202[1-9])$"
