#!/usr/bin/python3
""" holds user class"""
from .base_model import BaseModel


class User(BaseModel):
    """represent User"""

    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
