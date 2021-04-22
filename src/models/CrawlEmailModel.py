"""
        - ID
        - Email
        - FKEY(Crawl-History.ID)
"""
from peewee import *
from models import BaseModel, CrawHistoryModel

class CrawlEmailModel(BaseModel):
    crawl_email_id = AutoField()
    email = TextField()
    crawl_history_id = ForeignKeyField(CrawHistoryModel, to_field='crawl_history_id')