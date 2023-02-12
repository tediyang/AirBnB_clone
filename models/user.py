#!/usr/bin/python3
"""
    Import necessary modules
"""
from base_model import BaseModel


class User(BaseModel):
    """
        This class created a user
        with the class attributes
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
