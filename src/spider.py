import requests
import logging

from utility import RobotParser

class Spider():
    def __init__(self, domain):
        self.domain = domain
        self.rp = None
    
    def test(self):
        print(self.rp.allow)
        print(self.rp.disallow)
        print(self.rp.crawl_delay)

    def crawl_robots(self):
        req = requests.get(f'https://{self.domain}/robots.txt')
        if req.status_code == 200:
            self.rp = RobotParser(req.text)
            self.rp.parse()