#!/usr/bin/python3
"""test Review fille"""
import unittest
from models.Review import Review


class TestReview(unittest.TestCase):

    def test_review_attributes(self):
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_review_initialization(self):
        review_data = {
            "place_id": "123",
            "user_id": "456",
            "text": "This is a review"
        }
        review = Review(**review_data)
        self.assertEqual(review.place_id, review_data["place_id"])
        self.assertEqual(review.user_id, review_data["user_id"])
        self.assertEqual(review.text, review_data["text"])
