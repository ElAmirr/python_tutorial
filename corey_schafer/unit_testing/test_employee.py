import unittest
from unittest.mock import patch
from employee import Employee


class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    def setUp(self):
        print('setUp')
        self.emp1 = Employee('amir', 'othmani', 5000)
        self.emp2 = Employee('skandar', 'elothmani', 7000)

    def tearDown(self):
        print('tearDown\n')

    def test_email(self):
        print('test _email')
        self.assertEqual(self.emp1.email, 'amirothmani@gmail.com')
        self.assertEqual(self.emp2.email, 'skandarelothmani@gmail.com')

        self.emp1.first_name = 'oumaima'
        self.emp2.first_name = 'habib'

        self.assertEqual(self.emp1.email, 'oumaimaothmani@gmail.com')
        self.assertEqual(self.emp2.email, 'habibelothmani@gmail.com')

    def test_fullname(self):
        print('test_email')
        self.assertEqual(self.emp1.full_name, 'amir othmani')
        self.assertEqual(self.emp2.full_name, 'skandar elothmani')

        self.emp1.first_name = 'oumaima'
        self.emp2.first_name = 'habib'

        self.assertEqual(self.emp1.full_name, 'oumaima othmani')
        self.assertEqual(self.emp2.full_name, 'habib elothmani')

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp1.apply_raise()
        self.emp2.apply_raise()

        self.assertEqual(self.emp1.pay, 5500)
        self.assertEqual(self.emp2.pay, 7700)

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            scheduele = self.emp1.monthly_scheduele('May')
            mocked_get.assert_called_with('https://company.com/schafer/May')
            self.assertEqual(scheduele, 'Success')


if __name__ == '__main__':
    unittest.main()
