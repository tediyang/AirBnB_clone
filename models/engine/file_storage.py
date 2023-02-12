#!/usr/bin/python3

"""
    Import necessary modules
"""

import json
from json import JSONEncoder
from models.base_model import BaseModel


class FileStorage:
    """ This is the storage class, that stores in
        json file.
    """
    def __init__(self):
        """ Initialization of variables. """
        self.__file_path = "file.json"
        self.__objects = {}
        
    def all(self):
        """ Return the objects saved in the dictionary. """
        return self.__objects
    
    def new(self, obj):
        ''' obj: a dictionary of values
            this function adds new value to the object_dict
        '''
        key = f'{obj.__class__.__name__}.{obj.id}'
        value = obj
        self.__objects[key] = value
    
    def save(self):
        ''' save to json format (serialization) '''
        conv_obj = {obj: self.__objects[obj].to_dict() for obj in self.__objects.keys()}
        with open(self.__file_path, "w") as f:
            return json.dump(conv_obj, f)

    
    def reload(self):
        ''' load from a json file (deserialization) '''
        try:
            with open(self.__file_path) as f:
                loaded = json.load(f)
                ''' Below looping through the values (dict of keys and values),
                    calling the class function new (self.new) with the values
                    (dict of keys and values) passed as kwargs.
                '''
                for value in loaded.values():
                    cls_name = value["__class__"]
                    del value["__class__"]
                    self.new(eval(cls_name)(**value))

        except FileNotFoundError:
            return
