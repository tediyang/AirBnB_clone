#!/usr/bin/python3

"""test on BaseModel """
import re
import unittest
import datetime as DT
import uuid as UD
from models.base_model import BaseModel as BM

class Test_BaseModel(unittest.TestCase):
	""" testing the basemodel """

	@classmethod
	def setupClass(cls):
		"""class setup"""
		cls.mock = BM()

	@classmethod
	def tearDownClass(cls):
		"""tear down"""
		del cls.mock

	def test_id(self):
		"""test for uuid"""
		mock = self.mock
		self.assertIsInstance(mock, BM)
		self.assertIsInstance(mock.id, str)
		matches = re.fullmatch(r"\w{8}-\w{4}-\w{4}-\w{4}-w{12}", mock.id)

		self.assertTrue(matches)


 
	def test_str(self):
		""" special string representation """
		mock = self.mock
		correct_Format = "[{}] ({}) {}".format("BaseModel", mock.id, mock.__dict__)
		self.assertEqual(str(mock), correct_Format)

	def test_dict(self):
		""" dict repr """
		mock = self.mock
		test_dict = mock.to_dict()
		self.assertTrue("__class__" in test_dict)
		self.assertIsInstance(test_dict["__class__"], str)
		self.assertTrue("id" in test_dict)
		self.assertIsInstance(test_dict["id"], str)
		self.assertTrue("created_at" in test_dict)
		self.assertIsInstance(test_dict["created_at"], str)
		self.assertTrue("updated_at" in test_dict)
		self.assertIsInstance(test_dict["updated_at"], str)
		mock.test = 10
		test_dict = mock.to_dict()
		self.assertTrue("test" in test_dict)



if __name__ == "__main__":
	unittest.main()

