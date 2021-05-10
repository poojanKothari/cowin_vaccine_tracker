"""
Created on May 4, 2021

@author: poojan.kothari
"""

import json
import requests
import http.client

from util import constants


def base_session_method(absolute_url, base_url, pin_code, date):
    url = f"{base_url}{absolute_url}?pincode={pin_code}&date={date}"

    payload = {}
    headers = {
        'accept': 'application/json',
        'Accept-Language': 'hi_IN'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.json()

def base_session_method_new(absolute_url, base_url, pin_code, date):
    conn = http.client.HTTPSConnection("cdn-api.co-vin.in")
    payload = ''
    headers = {
        'accept': 'application/json',
        'Accept-Language': 'hi_IN'
    }
    conn.request("GET", f"/api/{absolute_url}?pincode={pin_code}&date={date}", payload,
                 headers)
    res = conn.getresponse()

    data = res.read()
    print("Status: {} and reason: {}".format(res.status, res.reason))
    print(f" Response obtained is {data}")
    return json.loads(data)

def check_day_session(pin_code, date):
    alert_list = []

    response = base_session_method_new(
        constants.day_session_by_pin,
        constants.base_url,
        pin_code, date)

    response_json = response
    sessions = response_json.get("sessions")

    if len(sessions) == 0:
        print(f"Daily: Center not open for date: {date} and pincode: {pin_code}")
        return alert_list, response

    for session in sessions:
        if ((session.get("min_age_limit") <= constants.default_min_age) and
                session.get("available_capacity") > 0):
            vaccine = session.get("vaccine")
            name = session.get("name")
            session_date = session.get("date")
            capacity = session.get("available_capacity")
            slot = ",".join(session.get("slots"))

            alert_list.append(
                f"Vaccine {vaccine} available in {name} on {session_date} during slots {slot} with capacity of {capacity}")

        if len(alert_list) == 0:
            print(f"Daily: Center not available for date: {date} and pincode: {pin_code}")
        return alert_list, response


def check_seven_days_session(pin_code, date):
    alert_list = []

    response = base_session_method_new(
        constants.seven_days_session_by_pin,
        constants.base_url,
        pin_code, date)

    response_json = response
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
