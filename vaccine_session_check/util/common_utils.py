"""
Created on May 4, 2021

@author: poojan.kothari
"""
import re
import time

from vaccine_session_check.util import constants, setu_utils, alert_utils


def get_pin_code():
    pin_code = ""
    is_valid_pin_code = False
    while not is_valid_pin_code:
        pin_code = str(
            input(
                f"> Enter Pin Code, Press enter to select default: {constants.default_pin_code}\n") or constants.default_pin_code)
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
            input(
                f"> Enter Date in format DD-MM-YYYY, press enter to select default:{constants.default_date}\n") or constants.default_date)
        if re.search(constants.date_regex, date):
            is_valid_date = True
        else:
            print("Invalid Date, Please Try again")
    return date


def get_recurrence_factor():
    try:
        rec_factor = int(
            input(
                f"> Enter Recurrence Frequency in seconds, press enter to select default: {constants.default_rec_fac} seconds \n") or constants.default_rec_fac)
    except Exception:
        print("Exception while taking input. Considering default value")
        rec_factor = constants.default_rec_fac
    return rec_factor


def start_week_tracker(pin_code, date, rec_factor):
    print(f"""
    Starting Weekly Trigger
        1. Pin Code => {pin_code},
        2. Date => {date},
        3. Recurrence factor => {rec_factor}
    """)
    while True:
        delay = rec_factor
        alert_list = []
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
        alert_list = []
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
