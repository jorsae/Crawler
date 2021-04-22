import logging

"""
    https://developers.google.com/search/docs/advanced/robots/robots_txt
"""

class RobotParser():
    def __init__(self, robot_text):
        self.robot_text = robot_text
        self.allow = []
        self.disallow = []
        self.crawl_delay = 0
    
    def parse(self):
        apply_to_this = True
        for line in self.robot_text.split('\n'):
            if line.lower().startswith('user-agent:'):
                line = self.parse_clean(line, 'user-agent:')
                apply_to_this = self.handle_user_agent(line)
            elif apply_to_this is False:
                continue
            elif line.lower().startswith('disallow:'):
                line = self.parse_clean(line, 'disallow:')
                self.disallow.append(line)
            elif line.lower().startswith('allow:'):
                line = self.parse_clean(line, 'allow:')
                self.allow.append(line)
            elif line.lower().startswith('crawl-delay:'):
                line = self.parse_clean(line, 'crawl-delay:')
                self.handle_crawl_delay(line)
                print(f'crawl-delay: {line}')
            else:
                print(f'{line=}')
    
    def parse_clean(self, line, start):
        return line[len(start):].strip()
    
    def handle_user_agent(self, line):
        if line is None:
            return True
        if '*' in line:
            return True
        else:
            return False
    
    def handle_crawl_delay(self, line):
        try:
            logging.info(f'handle_crawl_delay: {line}')
            self.crawl_delay = int(line)
        except Exception as e:
            logging.error(f'RobotParser.handle_crawl_delay: {e}')