import unittest
import volunteer_booking
import datetime
from .- import clinic_config
from googleapiclient.discovery import build
from io import StringIO
from unittest.mock import patch

class TestMe(unittest.TestCase):
    @patch("sys.stdin", StringIO("cape town\njohannesburg\njoburg"))
    def test_location(self):
        self.assertEqual(volunteer_booking.get_location(), "cape town")
        self.assertEqual(volunteer_booking.get_location(), "johannesburg")
        self.assertEqual(volunteer_booking.get_location(), "joburg")

    @patch("sys.stdin", StringIO("khwezi@student.wethinkcode.co.za\nosegobae@student.wethinkcode.co.za\nphmgagul@student.wethinkcode.co.za\nvgovende@student.wethinkcode.co.za\nkmolosiw@student.wethinkcode.co.za\ndubisi@student.wethinkcode.co.za"))
    def test_valid_email(self):
        self.assertEqual(volunteer_booking.get_user_email("khwezi"), "khwezi@student.wethinkcode.co.za")
        self.assertEqual(volunteer_booking.get_user_email("osegobae"), "osegobae@student.wethinkcode.co.za") 
        self.assertEqual(volunteer_booking.get_user_email("phmgagul"), "phmgagul@student.wethinkcode.co.za") 
        self.assertEqual(volunteer_booking.get_user_email("vgovende"), "vgovende@student.wethinkcode.co.za")
        self.assertEqual(volunteer_booking.get_user_email("kmolosiw"), "kmolosiw@student.wethinkcode.co.za")
        self.assertEqual(volunteer_booking.get_user_email("dubisi"), "dubisi@student.wethinkcode.co.za")


    def test_invalid_email(self):
        email = volunteer_booking.get_user_email("username")
        if '@' not in email:
            self.assertEqual(volunteer_booking.get_user_email("username"), 'Enter a valid email! ')
        if email.split('@')[1] != "student.wethinkcode.co.za":
            self.assertEqual(volunteer_booking.get_user_email("username"), 'Enter your student email.')
        elif email.split('@')[0] != "username":
            self.assertEqual(volunteer_booking.get_user_email("username"), 'Your username does not match the email!')

    
    def test_date_invalid():
        month_day = volunteer_booking.get_date()
        if ':' not in month_day:
            self.assertEqual(volunteer_booking.get_date(), 'Enter day in correct format.')
        if not month_day.split(':')[0].isdigit() or int(month_day[0]) < 0 or int(month_day[0]) > 12:
            self.assertEqual(volunteer_booking.get_date(), 'mm in date is not valid.')
        elif not month_day.split(':')[1].isdigit() or int(month_day[1]) < 0 or int(month_day[1]) > 31:
            self.assertEqual(volunteer_booking.get_date(), 'Enter valid date!')
        else:
            month_day = True

    
    def test_date_valid():
        month_day = '11:29'
        if ':' in month:
            if month_day.split(':')[0].isdigit() and month_day.split(':')[1].isdigit():
                self.assertEqual(volunteer_booking.validate_time(), '11:29')

    def test_validate_time():
        time = volunteer_booking.validate_time()
        if ':' not in time or int(time.split(':')[0]) > 23 or int(time.split(":")[1]) > 59:
            self.assertEqual(volunteer_booking.validate_time(), "Time is not valid")
        elif int(time.split(':')[1]) < 8 or int(time.split(':')[0]) > 17:
            self.assertEqual(volunteer_booking.validate_time(), "allowed times 08:00 - 17:00 ")
        else:
            time = True

    @patch("sys.stdin", StringIO("13:00"))
    def test_valid_time():
        self.assertEqual(volunteer_booking.validate_time(), '13:00')
        if ':' in time:
            if int(time.split(':')[0]) in range(00, 24) and int(time.split(':')[1]) in range(00, 60):
                self.assertEqual(volunteer_booking.validate_time(), True)

if __name__ == '__main__':
    unittest.main()    