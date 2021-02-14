#!/usr/bin/python3
"""BaseModel"""
from datetime import datetime
import uuid
import json


class BaseModel:
    """defines all common attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        """class constructor"""
        if kwargs:
            self.__dict__ = kwargs
            if 'created_at' in kwargs:
                self.created_at = datetime.strptime(
                    kwargs.get("created_at"), '%Y-%m-%dT%H:%M:%S.%f')
            if 'updated_at' in kwargs:
                self.updated_at = datetime.strptime(
                    kwargs.get("updated_at"), '%Y-%m-%dT%H:%M:%S.%f')
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            from models.__init__ import storage
            storage.new(self)

    def save(self):
        """
        Public instance method
        updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()
        from models.__init__ import storage
        storage.save()

    def __str__(self):
        """string representation"""
        return ("[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__))

    def to_dict(self):
        """
        Public instance method
        returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        new_dict = dict(self.__dict__)
        new_dict["__class__"] = str(type(self).__name__)
        new_dict["created_at"] = str(self.created_at.isoformat())
        new_dict["updated_at"] = str(self.updated_at.isoformat())
        return new_dict
