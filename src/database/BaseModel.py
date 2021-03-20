from peewee import *

import constants

DATABASE_FILE = '../poke-merch.sql'

database = SqliteDatabase(DATABASE_FILE)

class BaseModel(Model):
    class Meta:
        database = database