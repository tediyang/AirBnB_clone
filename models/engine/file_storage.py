"""
    Import necessary modules
"""

import json
from json import JSONEncoder
import datetime


class DateTimeEncoder(JSONEncoder):
    """ Convert datetime to json format """
    def default(self, obj):
        """ Override the default method """
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()


class FileStorage:
    """ This is the storage class, that stores in
        json file.
    """

    """ Initialization of private class variables. """
    __file_path = "file.json"
    __objects = {}
        
    def all(self):
        """ Return the objects saved in the dictionary. """
        return FileStorage.__objects
    
    def new(self, obj):
        ''' obj: a dictionary of values
            this function adds new value to the object_dict
        '''
        key = f'{obj["__class__"]}.{obj["id"]}'
        value = obj
        FileStorage.__objects[key] = value
    
    def save(self):
        ''' save to json format (serialization) '''
        conv_obj = {obj: FileStorage.__objects[obj] for obj in FileStorage.__objects.keys()}
        with open(FileStorage.__file_path, "w") as f:
            return json.dump(conv_obj, f, cls=DateTimeEncoder)

    
    def reload(self):
        ''' load from a json file (deserialization) '''
        try:
            with open(FileStorage.__file_path) as f:
                loaded = json.load(f)
                ''' Below looping through the values (dict of keys and values),
                    calling the class function new (self.new) with the values
                    (dict of keys and values) passed as kwargs.
                '''
                for value in loaded.values():
                    self.new(value)

        except FileNotFoundError:
            return
