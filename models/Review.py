#!/usr/bin/python3
"""holds review class"""
from .base_model import BaseModel


class Review(BaseModel):
    """Represent a review.

    Attributes:
        place_id (str): The Place id.
        user_id (str): The User id.
        text (str): The text of the review.
    """

    place_id: str = ""
    user_id: str = ""
    text: str = ""
