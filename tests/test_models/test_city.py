#!/usr/bin/python3
"""
    test city
"""
from models.city import City
from models.state import State
from models.base_model import BaseModel
import unittest


class test_City(unittest.TestCase):
    """
        test for city class
    """
    @classmethod
    def setUpClass(cls):
        """
            setup.
        """
        cls.mock_city = City()
        cls.mock_city.name = "test"
        cls.mock_city.state_id = State().id

    @classmethod
    def tearDownClass(cls):
        """
            tear down
        """
        del cls.mock_city

    def test_inheritance(self):
        """
            test proper inheritance
        """
        self.assertIsInstance(self.mock_city, BaseModel)
        self.assertTrue(hasattr(self.mock_city, "id"))
        self.assertTrue(hasattr(self.mock_city, "created_at"))
        self.assertTrue(hasattr(self.mock_city, "updated_at"))

    def test_attrs(self):
        """
            test attributes
        """
        self.assertTrue(hasattr(self.mock_city, "name"))
        self.assertTrue(hasattr(self.mock_city, "state_id"))
        
    def test_name(self):
        """
            test for name
        """
        self.assertTrue(self.mock_city.name, None)

    def test_state_id(self):
        """
            test for state_id
        """
        self.assertTrue(self.mock_city.state_id, None)
    

if __name__ == "__main__":
    unittest.main()
