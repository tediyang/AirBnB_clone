#!/usr/bin/python3
""" testing amenity """

import unittest
from models.amenity import Amenity as AT
from models.base_model import BaseModel as BM

class test_AT(unittest.TestCase):
	""" testing class """
	
	@classmethod
	def setupClass(cls):
		""" setting up process """
		cls.mock_amenity = AT()
		cls.mock_amenity.name = "test"

	@classmethod 
	def teardownClass(cls):
		""" tear down """
		del cls.mock_amenity

	def test_inheritance(self):
		""" testing for the inheritance """

		self.assertIsInstance(self.mock_amenity, BM)
		self.assertTrue(hasattr(self.mock_amenity, "id"))
		self.assertTrue(hasattr(self.mock_amenity, "created_at"))
		self.assertTrue(hasattr(self.mock_amenity, "updated_at"))


	def test_attrs(self):
		""" test for the attr or variables """
		self.assertTrue(hasattr(self.mock_amenity, "name"))


if __name__ == "__main__":
	unittest.main()
