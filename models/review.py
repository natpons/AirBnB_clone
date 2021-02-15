#!/usr/bin/python3
"""This module creates a class Review that inherits from BaseModel"""


class Review(BaseModel):
    """
    This is a User class with the public class attributes:
    - place_id: string - empty string: it will be the Place.id
    - user_id: string - empty string: it will be the User.id
    - text: string - empty string
    """

    place_id = ''
    user_id = ''
    text = ''
