#!/usr/bin/python3
"""
	importing modules
"""

import datetime as DT 
import uuid as UD 
class Base_model:
	"""
		This is the basemodel where i have all the 
		variables and method defined.
	"""

	def __init__(self, id, created_at, updated_at):
		self.id = str(UD.uuid4()) 
		self.created_at = DT.datetime.now()
		self.updated_at = self.created_at 


	def __str__(self):
		"""
			return should print: [<class name>] (<self.id>) <self.__dict__>
		"""
		return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

	def save(self):
		"""
			 updates the public instance attribute updated_at with the current datetime
		"""
		self.updated_at = DT.datetiem.now()

	def to_dict(self):
		"""
			returns a dictionary containing all keys/values of __dict__ of the instance.
		"""
		return {'id': self.id, 'created_at': self.created_at.isoformat(), 'updated_at': self.updated_at.isoformat(), '__class__': self.__class__.__name__}
			 




