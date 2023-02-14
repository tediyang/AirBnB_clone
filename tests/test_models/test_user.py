#!/usr/bin/python3
"""
    test for user
"""
import unittest
from models.user import User
from models.base_model import BaseModel


class test_User(unittest.TestCase):
    """
        User class tests
    """
    @classmethod
    def setUpClass(cls):
        """
            setup
        """
        cls.dummy_user = User()
        cls.dummy_user.email = ""
        cls.dummy_user.password = ""
        cls.dummy_user.first_name = ""
        cls.dummy_user.last_name = ""

    @classmethod
    def tearDownClass(cls):
        """
            tear down
        """
        del cls.dummy_user

    def test_inheritance(self):
        """
            test proper inheritance
        """
        self.assertIsInstance(self.dummy_user, BaseModel)
        self.assertTrue(hasattr(self.dummy_user, "id"))
        self.assertTrue(hasattr(self.dummy_user, "created_at"))
        self.assertTrue(hasattr(self.dummy_user, "updated_at"))

    def test_attrs(self):
        """
            test attributes
        """
        self.assertTrue(hasattr(self.dummy_user, "email"))
        self.assertTrue(hasattr(self.dummy_user, "password"))
        self.assertTrue(hasattr(self.dummy_user, "first_name"))
        self.assertTrue(hasattr(self.dummy_user, "last_name"))
        
    def test_name(self):
        """
            test for name
        """
        self.assertTrue(self.dummy_user.email, None)

    def test_password(self):
        """
            test for name
        """
        self.assertTrue(self.dummy_user.password, None)

    def test_first_name(self):
        """
            test for name
        """
        self.assertTrue(self.dummy_user.first_name, None)

    def test_last_name(self):
        """
            test for name
        """
        self.assertTrue(self.dummy_user.last_name, None)

        
if __name__ == "__main__":
    unittest.main()
