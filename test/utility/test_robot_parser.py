import pytest
import sys
sys.path.append('src')
from utility import *

def read_file(filename):
    pass

def test():
    rp = RobotParser('robot text')
    rp.parse()