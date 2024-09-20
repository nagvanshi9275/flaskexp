



"""
from mongoengine import Document, StringField, IntField, DateTimeField
import datetime

class User(Document):
    username = StringField(required=True, unique=True)
    email = StringField(required=True, unique=True)
    age = IntField(required=True)
    created_at = DateTimeField(default=datetime.datetime.utcnow)

    meta = {
        'collection': 'users'  # This will be the collection name in MongoDB Atlas
    }

"""

from mongoengine import Document, StringField, IntField, DateTimeField

import datetime

class User(Document):

  username = StringField(required=True, unique=True)
  email = StringField(required=True, unique=True)
  age = IntField(required=True)
  created_at = DateTimeField(default=datetime.datetime.utcnow)













