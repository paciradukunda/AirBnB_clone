#!/usr/bin/python3
"""test city fille"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):

    def test_city_attributes(self):
        """Test that City object has correct attributes"""
        city = City(state_id="CA", name="San Francisco")
        self.assertIsNotNone(city.id)
        self.assertEqual(city.state_id, "CA")
        self.assertEqual(city.name, "San Francisco")
