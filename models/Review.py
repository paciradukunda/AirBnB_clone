#!/usr/bin/python3
"""holds review class"""
from .base_model import BaseModel


class Review(BaseModel):
    """represent review """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """initializes review"""
        super().__init__(*args, **kwargs)
