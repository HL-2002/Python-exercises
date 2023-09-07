from working import convert
import unittest


def test_nine_to_five():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:30 PM") == "09:00 to 17:30"


def test_overnight():
    assert convert("10:21 PM to 3:59 AM") == "22:21 to 03:59"


class MyTestCase(unittest.TestCase):
    def test_error(self):
        self.assertRaises(ValueError, convert, "12:60 PM to 13 PM")