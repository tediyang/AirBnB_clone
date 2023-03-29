#!/usr/bin/python3
""" Place Module for AirBnB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from os import getenv
from models.review import Review
from models.amenity import Amenity

relationship_place_amen = Table("place_amenity", Base.metadata,
                 Column('place_id', String(60), ForeignKey('places.id'),
                 primary_key=True, nullable=False),
                 Column('amenity_id', String(60), ForeignKey('amenities.id'),
                 primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        places = relationship("Review",
    	                     backref=backref("place", cascade="all,delete"),
        	                 cascade="all, delete, delete-orphan",
            	             passive_deletes=True,
                	         single_parent=True)
        amenities = relationship("Amenity", secondary='place_amenity', viewonly=False, backref="place")

    else:
        @property
        def reviews(self):
            """ Return list of reviews with place.id"""
            # This prevents circular import
            from models import storage
            reviews_ = [obj for obj in storage.all(Review)
                         if obj.place_id == self.id]
            return reviews_

        @property
        def amenities(self):
            """ Return attribute amenities_ids """
            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj):
            """Appends an amenity id to the attribute
            amenity_id
            """
            if type(obj) == Amenity and obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)