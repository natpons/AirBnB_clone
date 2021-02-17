#!/usr/bin/python3
"""This module creates a class State that inherits from BaseModel"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    This is a User class with the public class attributes:
    - name: string - empty string
    """

    name = ''
