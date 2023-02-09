#!/usr/bin/python3
"""
	importing modules
"""

import datetime as DT 
import uuid as UD 
class BaseModel:
	"""
		This is the basemodel where i have all the 
		variables and method defined.
	"""

	def __init__(self):
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

	def to_dict(self):
		"""
			returns a dictionary containing all keys/values of __dict__ of the instance.
		"""
		return {'id': self.id, 'created_at': self.created_at.isoformat(), 'updated_at': self.updated_at.isoformat(), '__class__': self.__class__.__name__}
			 

def main():
	my_model = BaseModel()
	my_model.name = "My First Model"
	my_model.my_number = 89
	print(my_model)
	my_model.save()
	print(my_model)
	my_model_json = my_model.to_dict()
	print(my_model_json)
	print("JSON of my_model:")
	
	for key in my_model_json.keys():
		print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))


	

if __name__ == "__main__":
	main()




