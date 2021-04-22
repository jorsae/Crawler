from urllib.parse import urlparse
import requests
import os
from datetime import datetime
import logging

from models import *
from utility import *

"""
    Settings to have:
        database file
        log folder
        log file name
        max_redirects to allow (to make sure it can't be stuck in a loop)
        user-agent text
"""
# TODO: Move to settings.json
DATABASE_FILE = '../crawler.sql'
logFolder = '../logs'
logFile = 'crawler.log'

def main():
    # test()
    test_robots()

def test_robots():
    req = requests.get('https://www.vg.no/robots.txt')
    rp = RobotParser(req.text)
    rp.parse()

def test():
    url = 'http://direkte.vg.no/coronaviruset/videos/215460?wide=&utm_source=vgfront&utm_content=hovedlopet_row1_pos1'
    parsed = urlparse(url)
    dm, created = DomainModel.get_or_create(scheme=parsed.scheme, domain_name=parsed.netloc)
    chm, created = CrawHistoryModel.get_or_create(url='test', status_code=200, date_crawled=datetime.now(), domain_id=dm.domain_id)
    cqm, created = CrawlQueueModel.get_or_create(scheme='https', domain_name='test-domain', priority=0, referer='direkte.vg.no', date_added=datetime.now())
    cem, created = CrawlEmailModel.get_or_create(email='test_email@test.com', crawl_history_id=chm.crawl_history_id)

def setup_logging(folder, file):
    if not os.path.isdir(folder):
        os.makedirs(folder)
    handler = logging.FileHandler(filename=f'{folder}/{file}', encoding='utf-8', mode='a+')
    logging.basicConfig(handlers=[handler], level=logging.INFO, format='%(asctime)s %(levelname)s:[%(filename)s:%(lineno)d] %(message)s')

def setup_database():
    database.init(DATABASE_FILE)
    database.create_tables([DomainModel, CrawHistoryModel, CrawlQueueModel, CrawlEmailModel])

if __name__ == '__main__':
    setup_logging(logFolder, logFile)
    setup_database()
    main()