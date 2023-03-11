#!/usr/bin/python3
"""holds review class"""
from .base_model import BaseModel


class Review(BaseModel):
    """represent review"""

    place_id: str = ""
    user_id: str = ""
    text: str = ""

    def __init__(self, *args, **kwargs):
        """initializes review"""
        super().__init__(*args, **kwargs)
