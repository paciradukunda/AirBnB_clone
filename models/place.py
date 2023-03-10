#!/usr/bin/python3
"""holds class Place"""
from .base_model import BaseModel


class Place(BaseModel):
    """represant place """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwags)
    """initialize place"""
    super().__init__(*args, **kwargs)
