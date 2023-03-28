#!/usr/bin/python3
""" File Storage for AirBnB Clone Project """
""" Import necessary modules/ packages """

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review


class FileStorage:
    """
        This is the FileStorage class, that stores in
        json file.
    """
    # Assign the file path
    __file_path = "file.json"
    # Create an empty dictionary that will store the files
    # to be JSON dumped.
    __objects = {}

    def all(self, cls=None):
        """ Returns a dictionary of objectss currently in storage. """
        # If obj is None do nothing.
        if not cls:
            return FileStorage.__objects
        
        #create a dummy dictionary
        dummy = {}
        # loop into dictionary and check key if class name is present.
        for key, value in FileStorage.__objects.items():
            if cls.__name__ in key:
                dummy[key] = value
        return dummy

    def new(self, obj):
        ''' obj: class
            this function adds new value to the object_dict
        '''
        key = f'{obj.__class__.__name__}.{obj.id}'
        value = obj
        FileStorage.__objects[key] = value
    
    def save(self):
        ''' save to json format (serialization) '''
        # Get the keys in the dictionary and call the to_dict() with the value.
        # Remember the values are objects.
        conv_obj = {obj: FileStorage.__objects[obj].to_dict() for obj in FileStorage.__objects.keys()}
        with open(FileStorage.__file_path, "w") as f:
            return json.dump(conv_obj, f, indent=4)

    def delete(self, obj=None):
        ''' Delete object from the database '''
        # If obj is None do nothing.
        if not obj:
            return

        # Extract data to generate the key.
        key = f'{obj.__class__.__name__}.{obj.id}'
        del FileStorage.__objects[key]

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