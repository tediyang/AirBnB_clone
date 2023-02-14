#!/usr/bin/python3

"""
    Import necessary modules
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review


class FileStorage:
    """ This is the storage class, that stores in
        json file.
    """
    __file_path = "file.json"
    __objects = {}
        
    def all(self):
        """ Return the objects saved in the dictionary. """
        return FileStorage.__objects
    
    def new(self, obj):
        ''' obj: class
            this function adds new value to the object_dict
        '''
        key = f'{obj.__class__.__name__}.{obj.id}'
        value = obj
        self.__objects[key] = value
    
    def save(self):
        ''' save to json format (serialization) '''
        conv_obj = {obj: FileStorage.__objects[obj].to_dict() for obj in FileStorage.__objects.keys()}
        with open(FileStorage.__file_path, "w") as f:
            return json.dump(conv_obj, f, indent=4)

    
    def reload(self):
        ''' load from a json file (deserialization) '''
        try:
            with open(FileStorage.__file_path) as f:
                loaded = json.load(f)
                ''' Below looping through the values (dict of keys and values),
                    fetching the class name and deleting it from the value dict,
                    then calling the class function new (self.new) with the class
                    (after converted back to object using "eval") and passed values as kwargs.
                '''
                for value in loaded.values():
                    cls_name = value["__class__"]
                    del value["__class__"]
                    self.new(eval(cls_name)(**value)) #Using eval is critical

        except FileNotFoundError:
            return
