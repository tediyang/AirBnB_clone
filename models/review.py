#!/usr/bin/python3

""" importing neccessary modules """

from models.base_model import BaseModel

class Review(BaseModel):
	""" class attr """
	place_id = ""
	user_id = ""
	text = ""
