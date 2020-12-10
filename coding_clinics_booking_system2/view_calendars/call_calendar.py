import imports_f.imports as imports
import configure_the_system.check_token as check_token
# i think for the clinic calender,it has to be logged on at all times,
# or we have to switch between accounts to update them


def call_calendar_student(service, credentials):

    now = imports.datetime.datetime.now().isoformat() + 'Z' # 'Z' indicates UTC time
    days_later = (imports.datetime.datetime.now() + imports.datetime.timedelta(7)).isoformat() + 'Z'
    print('Getting the upcoming number of events(student)')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=1000, singleEvents=True,
                                        orderBy='startTime', timeMax=days_later).execute()
    events = events_result.get('items', [])

    return show_events_students(events)


def show_events_students(events):

    if not events: #Phumza did this whole part
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime')
        end = event['end'].get('dateTime')
        time_format = '%Y-%m-%dT%H:%M:%S+02:00'
        time_start = imports.datetime.datetime.strptime(start, time_format)
        time_end = imports.datetime.datetime.strptime(end, time_format)
        new_format = "%d %B %Y %H:%M"
        time_end_format = "%H:%M"
        new_start_time = time_start.strftime(new_format)
        new_end_time = time_end.strftime(time_end_format)
        print(f'{new_start_time} - {new_end_time}', event['summary'])


def call_calendar_clinic(service, credentials):#ash
    now = imports.datetime.datetime.now().isoformat() + 'Z' # 'Z' indicates UTC time
    days_later = (imports.datetime.datetime.now() + imports.datetime.timedelta(7)).isoformat() + 'Z'
    print('Getting the upcoming number of events(clinic)')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=1000, singleEvents=True,
                                        orderBy='startTime', timeMax=days_later).execute()
    events = events_result.get('items', [])

    return show_events_clinic(events)


def show_events_clinic(events):#ash

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime')
        end = event['end'].get('dateTime')
        time_format = '%Y-%m-%dT%H:%M:%S+02:00'
        time_start = imports.datetime.datetime.strptime(start, time_format)
        time_end = imports.datetime.datetime.strptime(end, time_format)
        new_format = "%d %B %Y %H:%M"
        time_end_format = "%H:%M"
        new_start_time = time_start.strftime(new_format)
        new_end_time = time_end.strftime(time_end_format)
        print(f'{new_start_time} - {new_end_time}', event['summary'])