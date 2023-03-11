#!/usr/bin/python3
"""
Contains the  amenity test suite
"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):

    def test_instance(self):
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def test_attributes(self):
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'name'))
        self.assertEqual(amenity.name, "")
