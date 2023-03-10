#!/usr/bin/python3
"""holds city class"""

from .base_model import BaseModel


class city(BaseModel):
    """Representation of city"""

    state_id: str = ""
    name: str = ""

    def __init__(self, *args, **kwargs):
        """ "initialize city"""
        super().__init__(*args, **kwargs)
