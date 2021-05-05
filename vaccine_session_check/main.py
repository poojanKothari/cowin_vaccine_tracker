"""
Created on May 4, 2021

@author: poojan.kothari
"""

from flask import Flask
from vaccine_session_check.util import common_utils, constants, day_tracker, week_tracker

app = Flask(__name__)

print(constants.banner)

pin_code = common_utils.get_pin_code()
date = common_utils.get_date()
rec_factor = common_utils.get_recurrence_factor()

day_tracker = day_tracker.DayTracker(pin_code, date, rec_factor)
week_tracker = week_tracker.WeekTracker(pin_code, date, rec_factor)

app.run(host="0.0.0.0", port='4010', debug=False, threaded=True)

print("Done")
