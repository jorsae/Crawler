import requests
import logging
from bs4 import BeautifulSoup

from utility import RobotParser

class Spider():
    def __init__(self, domain):
        self.domain = domain
        self.rp = None
        self.crawled_urls = 0
        self.run = True
        self.queue = set()
        self.queue.add(f'https://{self.domain}')
    
    def test(self):
        if self.rp is not None:
            print(self.rp.allow)
            print(self.rp.disallow)
            print(self.rp.crawl_delay)

    def crawl(self):
        while self.queue and self.run:
            url = self.queue.pop()
            req = self.request(url)
            if req is None:
                logging.info(f'Request is None: {url}')
                continue
            
            soup = BeautifulSoup(req.text)
            # TODO: Parse data
    
    def request(self, url):
        self.crawled_urls += 1
        
        try:
            req = requests.get(url, timeout=3)
        except requests.exceptions.Timeout as timeout:
            logging.debug(f'Request timed out: {url}')
            return None
        except Exception as e:
            logging.warning(f'Request exception: {e} | {url}')
            return None
        
        # TODO: Add to crawl history
        return req
    
    def crawl_robots(self):
        req = requests.get(f'https://{self.domain}/robots.txt')
        if req.status_code == 200:
            self.rp = RobotParser(req.text)
            self.rp.parse()
        else:
            # TODO: Do something if you can't find robots.txt
            pass