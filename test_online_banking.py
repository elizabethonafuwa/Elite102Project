import unittest
from unittest.mock import MagicMock
from backend import (
    generate_account_number,
    generate_pin,
    create_account
)

class TestBankingApp(unittest.TestCase):

    def test_generate_account_number(self):
        account_number = generate_account_number()
        self.assertIsInstance(account_number, int)
        self.assertTrue(100000 <= account_number <= 999999)

    def test_generate_pin(self):
        pin = generate_pin()
        self.assertIsInstance(pin, int)
        self.assertTrue(1000 <= pin <= 9999)

    def test_create_account(self):
        connection_mock = MagicMock()
        cursor_mock = MagicMock()
        connection_mock.cursor.return_value = cursor_mock

        create_account("John", "Doe")

        cursor_mock.execute.assert_called_once()

    # Add more tests for other functions

if __name__ == '__main__':
    unittest.main()
