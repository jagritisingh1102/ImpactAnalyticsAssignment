import unittest
from attendance_prob import Attendance


class TestAttendance(unittest.TestCase):
    def test_5_days(self):
        attendance = Attendance(5)
        self.assertEqual(attendance.probability_to_miss_graduation_ceremony(), "14/29")

    def test_10_days(self):
        attendance = Attendance(10)
        self.assertEqual(attendance.probability_to_miss_graduation_ceremony(), "372/773")

    def test_invalid_days_type(self):
        with self.assertRaises(TypeError):
            Attendance("five")

    def test_zero_days(self):
        attendance = Attendance(0)
        self.assertEqual(attendance.probability_to_miss_graduation_ceremony(), "0/1")

if __name__ == "__main__":
    unittest.main()