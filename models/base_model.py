#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
import uuid
from datetime import datetime

Base = declarative_base()


class BaseModel:
    """Base class for other classes to inherit from"""

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(
            DateTime, nullable=False,
            default=datetime.datetime.utcnow())

    updated_at = Column(
            DateTime, nullable=False,
            default=datetime.datetime.utcnow(),
            onupdate=datetime.datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Initialization of the base model"""
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.datetime.strptime(
                            value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__':
                    setattr(self, key, value)
        if 'id' not in kwargs:
            self.id = str(uuid.uuid4())

    def save(self):
        """Updates the attribute updated_at with the current datetime"""
        self.updated_at = datetime.datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def delete(self):
        """Deletes the current instance from the storage"""
        models.storage.delete(self)

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__"""
        dict_copy = self.__dict__.copy()
        if '_sa_instance_state' in dict_copy:
            del dict_copy['_sa_instance_state']
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        return dict_copy
