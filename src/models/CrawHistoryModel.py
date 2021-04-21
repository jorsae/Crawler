"""
        - ID
        - Full url
        - HTTP status code
        - Date crawled
        - FKEY(Websites.ID)
"""
from peewee import *
from models import BaseModel, DomainModel

class CrawHistoryModel(BaseModel):
    crawl_history_id = AutoField()
    url = TextField()
    status_code = SmallIntegerField()
    date_crawled = DateTimeField(null=True)
    domain_id = ForeignKeyField(DomainModel, to_field='domain_id')