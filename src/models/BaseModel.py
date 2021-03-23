from peewee import *

DATABASE_FILE = '../crawler.sql'

database = SqliteDatabase(DATABASE_FILE)

class BaseModel(Model):
    class Meta:
        database = database