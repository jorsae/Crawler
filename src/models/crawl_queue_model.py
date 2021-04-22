"""
        - ID
        - Scheme (http, https, etc)
        - Domain name (google.com, reddit.com)
        - Priority
        - referer (website that found this domain_name)
        - Date added to queue
"""
from peewee import *
from models import BaseModel

class CrawlQueueModel(BaseModel):
    crawl_queue_id = AutoField()
    scheme = CharField(8)
    domain_name = TextField()
    priority = SmallIntegerField()
    referer = TextField()
    date_added = DateTimeField(null=True)