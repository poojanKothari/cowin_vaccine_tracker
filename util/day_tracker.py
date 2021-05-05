"""
Created on May 4, 2021

@author: poojan.kothari
"""

from threading import Thread
from util import common_utils


class DayTracker(Thread):
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
        common_utils.start_day_tracker(self.pin_code, self.date, self.rec_factor)
