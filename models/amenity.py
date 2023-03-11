#!/usr/bin/python3
"""holds amenity class"""
from .base_model import BaseModel


class Amenity(BaseModel):
    """Represent an amenity.

    Attributes:
        name (str): The name of the amenity.
    """

    name: str = ""
