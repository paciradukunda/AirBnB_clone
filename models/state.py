#!/usr/bin/python3
"""holds class State"""
from .base_model import BaseModel


class State(BaseModel):
    """Represent a state.

    Attributes:
        name (str): The name of the state.
    """

    name: str = ""
