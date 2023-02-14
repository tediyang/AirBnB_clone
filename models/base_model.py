#!/usr/bin/python3

"""
	Importing modules
"""

import datetime as DT
import uuid as UD
#import models

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
			models.storage.new(self)

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
		return models.storage.save()

	def to_dict(self):
		"""
			returns a dictionary containing all keys/values of __dict__ of the instance.
		"""
		dic = {}
		dic["__class__"] = self.__class__.__name__

		for key, value in self.__dict__.items():
			if isinstance(value, DT.datetime):
				dic[key] = value.isoformat()
			else:
				dic[key] = value

		return dic
