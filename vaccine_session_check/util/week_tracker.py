"""
Created on May 4, 2021

@author: poojan.kothari
"""

from threading import Thread
from vaccine_session_check.util import common_utils


class WeekTracker(Thread):
    pin_code = None
    date = None
    rec_factor = None

    def __init__(self, pin_code, date, rec_factor):
        Thread.__init__(self)
        self.pin_code = pin_code
        self.date = date
        self.rec_factor = rec_factor
        self.daemon = True

        self.start()

    def run(self):
        common_utils.start_week_tracker(self.pin_code, self.date, self.rec_factor)
