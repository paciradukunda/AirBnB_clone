#!/usr/bin/python3
"""holds amenity class"""

from .base_model import BaseModel


class Amenity(BaseModel):
    """represent amenity"""

    name: str = ""

    def __init__(self, *args, **kwargs):
        """initialize amenity"""
        super().__init__(*args, **kwargs)
