"""
Created on May 4, 2021

@author: poojan.kothari
"""
import re
import time

from util import constants, alert_utils, setu_utils


def get_pin_code():
    pin_code = ""
    is_valid_pin_code = False
    while not is_valid_pin_code:
        pin_code = str(
            input(f"> Enter Pin Code, Press enter to select default: {constants.default_pin_code}\n")
            or constants.default_pin_code)

        if re.search(constants.pin_code_regex, pin_code):
            is_valid_pin_code = True
        else:
            print("Invalid Pin Code, Please Try again")
    return pin_code


def get_date():
    date = ""
    is_valid_date = False
    while not is_valid_date:
        date = str(
            input(f"> Enter Date in format DD-MM-YYYY, press enter to select default:{constants.default_date}\n")
            or constants.default_date)
        if re.search(constants.date_regex, date):
            is_valid_date = True
        else:
            print("Invalid Date, Please Try again")
    return date


def get_recurrence_factor():
    try:
        rec_factor = int(
            input(f"""> 
            Enter Recurrence Frequency in seconds, 
            Press enter to select default: {constants.default_rec_fac} seconds
            """)
            or constants.default_rec_fac)
    except Exception:
        print("Exception while taking input. Considering default value")
        rec_factor = constants.default_rec_fac
    return rec_factor


def get_window_type():
    try:
        window_type = int(
            input(
                f"""> 
                Enter Vaccine Window Type
                Type 1 for daily window
                Type 2 for weekly window
                press enter to select default: {constants.default_window_type} seconds
                """)
            or constants.default_window_type)
    except Exception:
        print("Exception while taking input. Considering default value")
        window_type = constants.default_window_type
    return window_type


def invoke_vaccine_tracker(window_type, pincode, date, rec_factor):
    if window_type == 2:
        start_week_tracker(pincode, date, rec_factor)
    else:
        start_day_tracker(pincode, date, rec_factor)


def start_week_tracker(pin_code, date, rec_factor):
    print(f"""
    Starting Weekly Trigger
        1. Pin Code => {pin_code},
        2. Date => {date},
        3. Recurrence factor => {rec_factor}
    """)
    while True:
        delay = rec_factor
        response = None
        try:
            alert_list, response = setu_utils.check_seven_days_session(pin_code, date)
            for alert in alert_list:
                alert_utils.trigger_alert("Weekly Vaccine Notification", alert, delay)
                print(alert)

        except Exception as e:
            print(f"""
            Exception occurred in week tracker.
            Response {response}.
            Error {e}""")

        finally:
            time.sleep(delay)


def start_day_tracker(pin_code, date, rec_factor):
    print(f"""
    Starting Daily Trigger
        1. Pin Code => {pin_code},
        2. Date => {date},
        3. Recurrence factor => {rec_factor}
    """)
    while True:
        delay = rec_factor
        response = None
        try:
            alert_list, response = setu_utils.check_day_session(pin_code, date)
            for alert in alert_list:
                alert_utils.trigger_alert("Daily Vaccine Notification", alert, delay)
                print(alert)

        except Exception as e:
            print(f"""
            Exception occurred in day tracker.
            Response {response}.
            Error {e}""")

        finally:
            time.sleep(delay)
