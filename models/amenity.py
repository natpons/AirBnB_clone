#!/usr/bin/python3
"""This module creates a class Amenity that inherits from BaseModel"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    This is a Amenity class with the public class attributes:
    - name: string - empty string
    """

    name = ''
