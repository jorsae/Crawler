"""
        - ID
        - Full url
        - HTTP status code
        - Date crawled
        - FKEY(Websites.ID)
"""
from peewee import *
from models import BaseModel

class CrawHistoryModel(BaseModel):
    domain_id = AutoField()