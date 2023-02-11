"""
    Import necessary modules
"""
import json

class FileStorage:
    """ This is the storage class, that stores in
        json.
    """
    def __init__(self):
        """ Initialization of variables. """
        self.__file_path = "file.json"
        self.__objects = {}
        
    def all(self):
        """ Return the objects saved in the dictionary. """
        return self.__objects
    
    def new(self, obj):
        ''' add new value to the object_dict '''
        key = f'{obj["__class__"]}.{obj["id"]}'
        value = obj
        self.__objects[key] = value
    
    def save(self):
        ''' save to json format (serialization) '''
        conv_obj = {obj: self.__objects[obj] for obj in self.__objects.keys()}
        for value in conv_obj.values():
            for key, value in value.items():
                if key in ['created_at', 'updated_at']:
                    value[key] = str(value)
        with open(self.__file_path, "w") as f:
            return json.dump(conv_obj, f,)

    
    def reload(self):
        ''' load from a json file (deserialization) '''
        try:
            with open(self.__file_path) as f:
                loaded = json.load(f)
                ''' Below looping through the values (dict of keys and values),
                    deleting the __class__ key and calling the base model (converted
                    to object using eval) with the values (dict of keys and values) 
                    passed as kwargs.
                '''
                for value in loaded.values():
                    del value["__class__"]
                    self.new(value)

        except FileNotFoundError:
            return
