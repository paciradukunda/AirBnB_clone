#!/usr/bin/python3
"""
Contains the TestPlaceDocs classes
"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    def setUp(self):
        """Sets up a Place instance for testing"""
        self.place = Place()

    def test_attributes(self):
        """Tests that Place attributes are set properly"""
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])
