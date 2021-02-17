#!/usr/bin/python3
"""This module creates a class FileStorage"""


import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns a DICTIONARY__objects of MODELS currently in storage"""
        return self.__objects

    def new(self, obj):
        """ADDS a new object TO storage DICTIONARY:
        sets in __objects the obj with key <obj class name>.id"""
        a = {obj.to_dict()['__class__'] + '.' + obj.id: obj}
        self.all().update(a)

    def save(self):
        """SAVES storage dictionary TO THE FILE:
        serializes __objects to the JSON file(path: __file_path)"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = FileStorage.__objects.copy()
            for key, value in temp.items():
                temp[key] = value.to_dict()
            json.dump(temp, f)

    def reload(self):
        """LOADS storage dictionary FROM FILE:
        - deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ; otherwise, do nothing.
        - if the file doesnt exist, no exception should be raised)"""
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, value in temp.items():
                    self.all()[key] = eval(value['__class__'])(**value)
        except FileNotFoundError:
            pass
