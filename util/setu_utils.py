"""
Created on May 4, 2021

@author: poojan.kothari
"""

import requests

from util import constants


def base_session_method(absolute_url, base_url, pin_code, date):
    url = f"{base_url}{absolute_url}?pincode={pin_code}&date={date}"

    payload = {}
    headers = {
        'accept': 'application/json',
        'Accept-Language': 'hi_IN'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response


def check_day_session(pin_code, date):
    alert_list = []

    response = base_session_method(
        constants.day_session_by_pin,
        constants.base_url,
        pin_code, date)

    response_json = response.json()
    sessions = response_json.get("sessions")

    for session in sessions:
        if ((session.get("min_age_limit") <= constants.default_min_age) and
                session.get("available_capacity") > 0):
            vaccine = session.get("vaccine")
            name = session.get("name")
            date = session.get("date")
            capacity = session.get("available_capacity")
            slot = ",".join(session.get("slots"))

            alert_list.append(
                f"Vaccine {vaccine} available in {name} on {date} during slots {slot} with capacity of {capacity}")

        if len(alert_list) == 0:
            print(f"Daily: Center not available for date: {date} and pincode: {pin_code}")
        return alert_list, response


def check_seven_days_session(pin_code, date):
    alert_list = []

    response = base_session_method(
        constants.seven_days_session_by_pin,
        constants.base_url,
        pin_code, date)

    response_json = response.json()
    centers = response_json.get("centers")
    if len(centers) == 0:
        print(f"Center not open for week {date} and {pin_code}")
        return alert_list, response
    else:
        for center in centers:
            name = center.get("name")
            for session in center.get("sessions"):
                if ((session.get("min_age_limit") <= constants.default_min_age) and
                        session.get("available_capacity") > 0):
                    date = session.get("date")
                    vaccine = session.get("vaccine")
                    capacity = session.get("available_capacity")
                    slot = ",".join(session.get("slots"))
                    alert_list.append(
                        f"Vaccine {vaccine} available in {name} on {date} during slots {slot} with capacity of {capacity}")

        if len(alert_list) == 0:
            print(f"Weekly: Center not available for date: {date} and pincode: {pin_code}")

        return alert_list, response
