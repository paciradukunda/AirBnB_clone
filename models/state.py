#!/usr/bin/python3
"""holds class State"""

from . import BaseModel


class State(BaseModel):
    """Representation of state"""
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)
