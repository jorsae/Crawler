import pytest
import sys
sys.path.append('src')
from utility import *
import os

def read_file(filename):
    return open(f'test/utility/test-data/{filename}', 'r').read()

testdata_parse_allow = [
    ('vg_robots.txt', []),
    ('reddit_robots.txt', ['/', '/sitemaps/*.xml', '/posts/*'])
    ]

@pytest.mark.parametrize("file, expected", testdata_parse_allow)
def test_parse_allow(file, expected):
    data = read_file(file)
    rp = RobotParser(data)
    rp.parse()
    assert(rp.allow) == expected