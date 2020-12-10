#!/usr/bin/python3

from configure_the_system import check_token
from terminal_prompts import helps
from make_a_booking.clinic_config import main
from make_a_booking.clinic_config import call_calendar2
from volunteer_for_a_slot.volunteer_booking import create_event
from sys import argv
import os

"""
if __name__ == "__main__":
    check_token.check_if_token_exists()
    helps()
"""

if len(argv) != 2:
    helps() 
elif len(argv) == 2:
    if "help" in argv:
        helps()
    elif "login" in argv:
        check_token.check_if_token_exists()
    elif "view_calendar" in argv:
        call_calendar2()
    elif "make_booking" in argv:
        create_event()
    else:
        helps()