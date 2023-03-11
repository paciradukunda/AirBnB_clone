#!/usr/bin/python3
"""test user fille"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    def test_user_attributes(self):
        user = User(
    email      = "user@example.com",
    password   = "password123",
    first_name = "John",
    last_name  = "Doe"
)


        self.assertEqual(user.email, "user@example.com")
        self.assertEqual(user.password, "password123")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")


if __name__ == '__main__':
    unittest.main()
