#!/usr/bin/python3
"""holds class Place"""
from .base_model import BaseModel


class Place(BaseModel):
    """represant place"""

    city_id: str = ""
    user_id: str = ""
    name: str = ""
    description: str = ""
    number_rooms: int = 0
    number_bathrooms: int = 0
    max_guest: int = 0
    price_by_night: int = 0
    latitude: float = 0.0
    longitude: float = 0.0
    amenity_ids: list = []

    def __init__(self, *args, **kwargs):
        """initialize place"""
        super().__init__(*args, **kwargs)
