"""    Domains/Websites:
        - ID
        - Scheme (http, https, etc)
        - Domain-name (urllib.parse.netloc)
        - Times crawled
        - First time crawled
        - Last time crawled
"""
from peewee import *
from models import BaseModel

class DomainModel(BaseModel):
    domain_id = AutoField()
    scheme = CharField(8)
    domain_name = TextField()
    times_crawled = SmallIntegerField(default=0)
    first_time_crawled = DateTimeField(null=True)
    last_time_crawled = DateTimeField(null=True)

    class Meta:
        indexes = (
            (('scheme', 'domain_name'), True),
        )