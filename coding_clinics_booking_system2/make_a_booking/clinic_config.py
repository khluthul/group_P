from __future__ import print_function

import pickle
import os.path
# from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import imports_f.imports as imports
import view_calendars.call_calendar as call
from os.path import expanduser
home = expanduser("~")
# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']

def call_calendar2():
    if imports.os.path.exists('make_a_booking/.hidden_folder/.clinic_token.pkl'):
        credentials2 = imports.pickle.load(open('make_a_booking/.hidden_folder/.clinic_token.pkl', 'rb'))
    else:
        credentials2 = flow.run_local_server(port=0)
    service2 = imports.build("calendar", "v3", credentials=credentials2)
    call.call_calendar_clinic(service2, credentials2)

def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('make_a_booking/.hidden_folder/.clinic_token.pkl'):
        with open('make_a_booking/.hidden_folder/.clinic_token.pkl', 'rb') as token:
            creds = pickle.load(token)
            #print('clinic\'s token loaded')
            # call_calendar2()
            
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'make_a_booking/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('make_a_booking/.hidden_folder/.clinic_token.pkl', 'wb') as token:
            pickle.dump(creds, token)

    # service = build('calendar', 'v3', credentials=creds)
    return creds



# if __name__ == '__main__':
    # main()
