class RobotParser():
    def __init__(self, robot_text):
        self.robot_text = robot_text
        self.allow = []
        self.disallow = []
    
    def parse(self):
        self.robot_text = self.robot_text.lower()
        apply_to_this = True
        for line in self.robot_text.split('\n'):
            if line.startswith('user-agent:'):
                line = self.parse_clean(line, 'user-agent:')
                apply_to_this = self.handle_user_agent(line)
            elif apply_to_this is False:
                continue
            elif line.startswith('disallow:'):
                line = self.parse_clean(line, 'disallow:')
                self.disallow.append(line)
            elif line.startswith('allow:'):
                line = self.parse_clean(line, 'allow:')
                self.allow.append(line)
            else:
                print(f'{line=}')
    
    def parse_clean(self, line, start):
        if line.startswith(start):
            return line[len(start):].strip()
        else:
            return None
    
    def handle_user_agent(self, line):
        if '*' in line:
            return True
        else:
            return False