'''
here we will configure the system to connect to 
our WeThinkCode_ Google calendar,
and the Code Clinic Google calendar.
'''
from os.path import expanduser
home = expanduser("~")

# import sys
# sys.path.insert(1, home+'coding_clinics_booking_system2/imports')

import imports_f.imports as imports
import view_calendars.call_calendar as call

# print(home)
def check_if_token_exists():
    """
    [checks if token exists on pc]

    Returns:
        [load_token()]: [if token exists]
        [create_token()]: [if token is non exisent]
    """
    if imports.os.path.exists(home+"/.token.pkl"):
        # print('True')
        load_token()
    else:
        # print('False')
        create_token()


def call_calendar():
    if imports.os.path.exists(home+"/.token.pkl"):
        credentials = imports.pickle.load(open(home+"/.token.pkl", "rb"))
    else:
        credentials = flow.run_local_server(port=0)
    service = imports.build("calendar", "v3", credentials=credentials)
    call.callcalendar_student(service, credentials)


def load_token():
    """
    [loads the token if check_if_token_exists() returns True]
    """
    credentials = imports.pickle.load(open(home+"/.token.pkl", "rb"))
    print("Student's token already exists!")
    print('Student\'s token loaded')
    # call_calendar()

scopes = ['https://www.googleapis.com/auth/calendar']
flow = imports.InstalledAppFlow.from_client_secrets_file('client_secret.json', scopes)


def create_token():
    """
    [creates a token if check_if_token_exists() returns False]
    [save creadentials for the next login]
    """
    credentials = flow.run_local_server(port=0)
    # save credentials
    imports.pickle.dump(credentials,open(home+"/.token.pkl", "wb"))
    
    print('student token created')
    # call_calendar()