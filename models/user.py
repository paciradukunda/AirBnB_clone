#!/usr/bin/python3
""" holds user class"""
from .base_model import BaseModel


class User(BaseModel):
    """represent User"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
