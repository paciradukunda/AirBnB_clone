#!/usr/bin/python3
"""holds amenity class"""

from .base_model import BaseModel


class amenity(BaseModel):
    """represent amenity"""
    name = ""

    def __init__(self, *args, **kwargs):
        """initialize amenity"""
        super().__init__(*args, **kwargs)
