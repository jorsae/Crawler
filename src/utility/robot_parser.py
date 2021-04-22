class RobotParser():
    def __init__(self, robot_text):
        self.robot_text = robot_text
        self.allow = []
        self.disallow = []
    
    def parse(self):
        self.robot_text = self.robot_text.lower()
        apply_to_this = True
        for line in self.robot_text.split('\n'):
            if line.startswith('user-agent'):
                apply_to_this = self.handle_user_agent(line)
            elif line.startswith('disallow'):
                print('disallow')
            elif line.startswith('allow'):
                print('allow')
            else:
                print(f'{line=}')
    
    def handle_user_agent(self, line):
        line = line.replace('user-agent:', '')
        line = line.strip()
        # TODO: Have this support a name
        if '*' in line:
            return True
        else:
            return False