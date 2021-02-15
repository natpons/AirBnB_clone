#!/usr/bin/python3
"""This module creates a class User that inherits from BaseModel"""


class User(BaseModel):
    """
    This is a User class with the public class attributes:
    - email, password, first_name, last_name: string - empty string
    """

    email = ''
    password = ''
    first_name = ''
    last_name = ''
