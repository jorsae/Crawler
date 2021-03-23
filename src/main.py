from urllib.parse import urlparse
import os
import logging
from models import *

def main():
    test()

def test():
    url = 'https://direkte.vg.no/coronaviruset/videos/215460?wide=&utm_source=vgfront&utm_content=hovedlopet_row1_pos1'
    parsed = urlparse(url)
    dm, created = DomainModel.get_or_create(scheme=parsed.scheme, domain_name=parsed.netloc)
    dm, created = DomainModel.get_or_create(scheme=parsed.scheme, domain_name=parsed.netloc)

def setup_logging():
    logFolder = '../logs'
    logFile = 'crawler.log'
    if not os.path.isdir(logFolder):
        os.makedirs(logFolder)
    handler = logging.FileHandler(filename=f'{logFolder}/{logFile}', encoding='utf-8', mode='a+')
    logging.basicConfig(handlers=[handler], level=logging.INFO, format='%(asctime)s %(levelname)s:[%(filename)s:%(lineno)d] %(message)s')

def setup_database():
    database.create_tables([DomainModel])

if __name__ == '__main__':
    setup_logging()
    setup_database()
    main()