"""
Created on May 3, 2021

@author: poojan.kothari
"""

from win10toast import ToastNotifier

toaster = ToastNotifier()


def trigger_alert(title, message, duration):
    toaster.show_toast(
        title,
        message,
        duration=duration,
        icon_path=r"assets\images\largest-vaccine-banner.ico",
        threaded=True)
