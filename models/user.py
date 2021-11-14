#!/usr/bin/python3
import uuid
from datetime import datetime
from models import storage
from models.base_model import BaseModel

class User(BaseModel):
   
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        '__init__ method for user'
        if len(kwargs) > 0:
            self.__dict__ = kwargs
        else:
            super().__init__(self)
