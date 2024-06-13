#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""


import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {
        'BaseModel': BaseModel, 'User': User, 'Place': Place,
        'State': State, 'City': City, 'Amenity': Amenity, 'Review': Review
        }


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is None:
            return FileStorage.__objects
        else:
            filtered_objects = {}
            for key, obj in FileStorage.__objects.items():
                if isinstance(obj, cls):
                    filtered_objects[key] = obj
        return filtered_objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file"""
        json_objects = {}
        for key in self.__objects:
            json_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            with open(self.__file_path, 'r') as f:
                jo = json.load(f)
                for key in jo:
                    self.__objects[key] = classes[jo[key]["__class__"]](**jo[key])
        except:
            pass

    def delete(self, obj=None):
        """Deletes obj from __objects if it's inside"""
         if obj is not None:
             key = obj.__class__.__name__ + '.' + obj.id
             if key in self.__objects:
                 del self.__objects[key]

    def close(self):
        """Call reload() method for deserializing the JSON file to objects"""
        self.reload()
