"""[here we get the user input]
"""
import sys
from configure_the_system.check_token import call_calendar
from make_a_booking.clinic_config import call_calendar2
from volunteer_for_a_slot.volunteer_booking import create_event
from make_a_booking.student_booking import create_booking

def helps():
    #print('')
    #print('what would you like to do next?')
    print('list of arguments:\n\n\
login\n\
view_calendar(clinic)\n\
make_a_booking\n\
volunteer_for_a_booking\n\
logout')
    #user_response = input()
    """
    if user_response.lower() == '1':
        call_calendar2()
        helps()
    elif user_response.lower() == '2':
        create_booking()
        helps()
    elif user_response.lower() == '3':
        create_event()
        helps()
    else:
        print('enter a valid number stupid')
        helps()
    """