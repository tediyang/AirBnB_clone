#!/usr/bin/python3

"""
	Importing modules
"""

import datetime as DT
import uuid as UD

storage = __import__('__init__').storage

class BaseModel:
	"""
		This is the basemodel where all the 
		variables and method defined and other classes
        	will inherit from.
	"""

	def __init__(self, *args, **kwargs):
		"""
        	Initialization of the variabes
		"""
		if len(kwargs) > 0:
			for key, value in kwargs.items():
				if key in ['created_at', 'updated_at']:
					setattr(self, key, DT.datetime.fromisoformat(value))
				elif key != "__class__":
					setattr(self, key, value)
		else:
			self.id = str(UD.uuid4())
			self.created_at = DT.datetime.now()
			self.updated_at = self.created_at
			storage.new(self)

	def __str__(self):
		"""
			return should print: [<class name>] (<self.id>) <self.__dict__>
		"""
		return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

	def save(self):
		"""
			updates the public instance attribute updated_at with the current datetime
		"""
		self.updated_at = DT.datetime.now()
		return storage.save()

	def to_dict(self):
		"""
			returns a dictionary containing all keys/values of __dict__ of the instance.
		"""
		if "__class__" not in self.__dict__.keys():
			self.__dict__["__class__"] = self.__class__.__name__
		self.__dict__['created_at'] = self.created_at.isoformat()
		self.__dict__['updated_at'] = self.updated_at.isoformat()

		return self.__dict__



if __name__ == "__main__":
	all_objs = storage.all()
	print("-- Reloaded objects --")
	for obj_id in all_objs.keys():
		obj = all_objs[obj_id]
		print(obj)

	print("-- Create a new object --")
	my_model = BaseModel()
	my_model.name = "My_First_Model"
	my_model.my_number = 89
	my_model.save()
	print(my_model)
