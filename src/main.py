from urllib.parse import urlparse
import os
from datetime import datetime
import logging

from models import *

# TODO: Move to settings.json
DATABASE_FILE = '../crawler.sql'
logFolder = '../logs'
logFile = 'crawler.log'

def main():
    test()

def test():
    url = 'http://direkte.vg.no/coronaviruset/videos/215460?wide=&utm_source=vgfront&utm_content=hovedlopet_row1_pos1'
    parsed = urlparse(url)
    dm, created = DomainModel.get_or_create(scheme=parsed.scheme, domain_name=parsed.netloc)
    chm, created = CrawHistoryModel.get_or_create(url='test', status_code=200, date_crawled=datetime.now(), domain_id=dm.domain_id)

def setup_logging():
    if not os.path.isdir(logFolder):
        os.makedirs(logFolder)
    handler = logging.FileHandler(filename=f'{logFolder}/{logFile}', encoding='utf-8', mode='a+')
    logging.basicConfig(handlers=[handler], level=logging.INFO, format='%(asctime)s %(levelname)s:[%(filename)s:%(lineno)d] %(message)s')

def setup_database():
    database.init(DATABASE_FILE)
    database.create_tables([DomainModel, CrawHistoryModel])

if __name__ == '__main__':
    setup_logging()
    setup_database()
    main()