#!/usr/bin/python3
"""
    test place
"""
from models.place import Place
from models.city import City
from models.user import User
from models.base_model import BaseModel
import unittest


class test_Place(unittest.TestCase):
    """
        test for Place class
    """
    @classmethod
    def setUpClass(cls):
        """
            setup
        """
        cls.dummy_city = Place()
        cls.dummy_city.city_id = None
        cls.dummy_city.user_id = None
        cls.dummy_city.name = None
        cls.dummy_city.description = None
        cls.dummy_city.number_rooms = None
        cls.dummy_city.number_bathrooms = None
        cls.dummy_city.max_guest = None
        cls.dummy_city.price_by_night = None
        cls.dummy_city.latitude = None
        cls.dummy_city.longitude = None
        cls.dummy_city.amenity_ids = None


    @classmethod
    def tearDownClass(cls):
        """
            tear down
        """
        del cls.dummy_city

    def test_inheritance(self):
        """
            test proper inheritance
        """
        self.assertIsInstance(self.dummy_city, BaseModel)
        self.assertTrue(hasattr(self.dummy_city, "id"))
        self.assertTrue(hasattr(self.dummy_city, "created_at"))
        self.assertTrue(hasattr(self.dummy_city, "updated_at"))

    def test_attrs(self):
        """
            test attributes
        """
        self.assertTrue(hasattr(self.dummy_city, "city_id"))
        self.assertTrue(hasattr(self.dummy_city, "user_id"))
        self.assertTrue(hasattr(self.dummy_city, "name"))
        self.assertTrue(hasattr(self.dummy_city, "description"))
        self.assertTrue(hasattr(self.dummy_city, "number_rooms"))
        self.assertTrue(hasattr(self.dummy_city, "number_bathrooms"))
        self.assertTrue(hasattr(self.dummy_city, "max_guest"))
        self.assertTrue(hasattr(self.dummy_city, "price_by_night"))
        self.assertTrue(hasattr(self.dummy_city, "latitude"))
        self.assertTrue(hasattr(self.dummy_city, "longitude"))
        self.assertTrue(hasattr(self.dummy_city, "amenity_ids"))

    def test_city_id(self):
        """
            test for city_id
        """
        self.assertTrue(self.dummy_city.city_id, None)

    def test_user_id(self):
        """
            test for user_id
        """
        self.assertTrue(self.dummy_city.user_id, None)

    def test_description(self):
        """
            test for description
        """
        self.assertTrue(self.dummy_city.description, None)

    def test_number_rooms(self):
        """
            test for number_rooms
        """
        self.assertTrue(self.dummy_city.number_rooms, None)

    def test_number_bathrooms(self):
        """
            test for number_bathrooms
        """
        self.assertTrue(self.dummy_city.number_bathrooms, None)

    def test_max_guest(self):
        """
            test for max_guest
        """
        self.assertTrue(self.dummy_city.max_guest, None)

    def test_price_by_night(self):
        """
            test for price_by_night
        """
        self.assertTrue(self.dummy_city.price_by_night, None)

    def test_latitude(self):
        """
            test for latitude
        """
        self.assertTrue(self.dummy_city.latitude, None)

    def test_longitude(self):
        """
            test for longitude
        """
        self.assertTrue(self.dummy_city.longitude, None)

    def test_amenities(self):
        """
            test for amenities
        """
        self.assertTrue(self.dummy_city.amenity_ids, None)


if __name__ == "__main__":
    unittest.main()
