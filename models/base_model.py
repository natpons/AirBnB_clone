#!/usr/bin/python3
"""This module defines class BaseModel for all models in airbnb clone"""


import uuid
from datetime import datetime
import models


class BaseModel:
    """
    Defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes class BaseModel
        """
        self.id = str(uuid.uuid4())
        self.updated_at = datetime.utcnow()
        self.created_at = datetime.utcnow()

        if kwargs != {}:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            models.storage.new(self)

    def __str__(self):
        """Returns a string representation of the instance"""
        return("[{}] ({}) {}".format(
                    self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """Convert INSTANCE into DICT FORMAT containing all keys/values :
        create a dictionary representation with "simple object type
        of our BaseModel"""
        basemodel_dict = {}
        basemodel_dict["__class__"] = self.__class__.__name__

        if self.__dict__:
            for key, value in self.__dict__.items():
                if isinstance(value, datetime):
                    value = value.isoformat()
                basemodel_dict[key] = value
        return basemodel_dict
