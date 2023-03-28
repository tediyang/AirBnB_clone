#!/usr/bin/python3

"""
	Importing modules
"""

import datetime as DT
import uuid as UD
import models
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, DateTime


# using sqlalchemy base model.
Base = declarative_base()


class BaseModel:
	"""
		This is the BaseModel where all the
		variables and method defined and other classes
        will inherit from.
	"""
	id = Column(String(60), primary_key=True, nullable=False)
	created_at = Column(DateTime, default=DT.datetime.utcnow(), nullable=False)
	updated_at = Column(DateTime, default=DT.datetime.utcnow(), nullable=False)

	def __init__(self, *args, **kwargs):
		"""
        	Initialization of the variabes
		"""
		if kwargs:
			for key, value in kwargs.items():
				if key in ['created_at', 'updated_at']:
					setattr(self, key, DT.datetime.fromisoformat(value))
				elif key != "__class__":
					setattr(self, key, value)
		else:
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
		self.updated_at = DT.datetime.now()
		models.storage.new(self)
		return models.storage.save()

	def delete(self):
		"""
			Delete the object in the storage.
		"""
		return models.storage.delete(self)

	def to_dict(self):
		"""
			returns a dictionary containing all keys/values of __dict__ of the instance.
		"""
		dic = {}
		dic["__class__"] = self.__class__.__name__

		for key, value in self.__dict__.items():
			if key == "_sa_instance_state":
				pass
			elif isinstance(value, DT.datetime):
				dic[key] = value.isoformat()
			else:
				dic[key] = value

		return dic