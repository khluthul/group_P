
from volunteer_for_a_slot.volunteer_booking import create_event
from volunteer_for_a_slot import volunteer_booking 

service = volunteer_booking.service

def patient_booking(email, id):
    event = service.events().get(calendarId='primary', eventId=id).execute()
    event['attendees'].append({'email': email})
    event = service.events().update(calendarId='primary',
                                    eventId=event['id'], body=event).execute()
    print("updated event")
    print('Event created: %s' % (event.get('htmlLink')))
    print("id: ", event['id'])
    print("summary: ", event['summary'])
    print("starts at: ", event['start']['dateTime'])
    print("ends at: ", event['end']['dateTime'])
    print(event)
    return True

def create_booking():
    email = input("enter your email: ")
    id = input("enter the event id: ")
    patient_booking(email,id)