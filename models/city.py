#!/usr/bin/python3
"""holds city class"""

from . import BaseModel


class city(BaseModel):
    """Representation of city"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """"initialize city"""
        super().__init__(*args, **kwargs)
