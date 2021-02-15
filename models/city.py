#!/usr/bin/python3
"""This module creates a class State that inherits from BaseModel"""


class City(BaseModel):
    """
    This is a City class with the public class attributes:
    - state_id: string - empty string: it will be the State.id
    - name: string - empty string
    """

    state_id = ''
    name = ''
