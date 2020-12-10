from make_a_booking import clinic_config
import datetime
from googleapiclient.discovery import build

creds = clinic_config.main()


service = build('calendar', 'v3', credentials=creds)


def doctor_booking(location, des, username, email, month, day, time):

    h, m = time.split(":")
    start = datetime.time(int(h), int(m), 0)
    delta = datetime.timedelta(minutes=30)
    end = (datetime.datetime.combine(
        datetime.date(1, 1, 1), start) + delta).time()
    print(end)

    year_month = datetime.datetime.now()
    start_time = str(year_month)[:5]+month+"-" + day+"T" + str(start)
    end_time = str(year_month)[:5]+month+"-" + day + "T" + str(end)

    event = {
        "conferenceDataVersion": 1,
        'summary': "Volunteer",
        'location': location,
        'description': des,

        'autoAddHangouts': 'true',
        'start': {
            'dateTime': start_time,
            'timeZone': 'Africa/Johannesburg',
        },
        'end': {
            'dateTime': end_time,
            'timeZone': 'Africa/Johannesburg',
        },


        "attendees": [{"email": [email, ""]}],
        'guestsCanModify': False,
        'sendUpdates': 'all',

        'reminders': {
            'useDefault': False,

            'overrides': [
                {'method': 'email', 'minutes': 24 * 60},
                {'method': 'popup', 'minutes': 10},
            ],
        },
        "conferenceData": {
            "createRequest": {
                "requestId": "someRandomKey"
            }
        }
    }

    event = service.events().insert(calendarId='primary', body=event).execute()

    print()
    print('Event created: %s' % (event.get('htmlLink')))
    print("id: ", event['id'])
    print("summary: ", event['summary'])
    print("starts at: ", datetime.datetime.strptime(
        event["start"]["dateTime"], "%Y-%m-%dT%H:%M:%S%z"))
    print("ends at: ", datetime.datetime.strptime(
        event["end"]["dateTime"], "%Y-%m-%dT%H:%M:%S%z"))
    return True


def get_user_email(username):
    while(True):
        email = input("Enter User email: ")
        if '@' not in email:
            print('Enter a valid email! ')
            continue
        trailing_part = email.split('@')
        if trailing_part[1] != "student.wethinkcode.co.za":
            print('Enter your student email.')
            continue
        elif trailing_part[0] != username:
            print('Your username does not match the email!')
            exit(1)
        return email


def get_date():
    year_month = datetime.datetime.now()
    print('Year month is: ', year_month)
    while True:
        month_day = input("Enter day in this format, mm:dd : ")
        if ':' not in month_day:
            print('Enter day in correct format.')
            continue
        month_day = month_day.split(':')
        if not month_day[0].isdigit() or int(month_day[0]) < 0 or int(month_day[0]) > 12:
            print('mm in date is not valid.')
            continue
        elif not month_day[1].isdigit() or int(month_day[1]) < 0 or int(month_day[1]) > 31:
            print('Enter valid date!')
            continue
        else:
            break
    return month_day[0], month_day[1]


def get_location():
    while True:
        location = input("Enter location between Johannesburg and Cape Town: ").lower()
        cities = ['johannesburg', 'cape town', 'joburg']
        if location in cities:
            return location


def validate_time():
    while True:
        time = input("time HH:MM ")
        if ':' not in time or int(time.split(':')[0]) > 23 or int(time.split(":")[1]) > 59:
            print("Time is not valid")
        elif int(time.split(':')[0]) < 8 or int(time.split(':')[0]) > 17:
            print("allowed times 08:00 - 17:00 ")
        else:
            break
    return time


def create_event():
    location = get_input()
    des = input("Description: ")
    username = input("Enter username: ")
    email = get_user_email(username)
    month, day = get_date()
    time = validate_time()
    doctor_booking(location, des, username, email, month, day, time)
