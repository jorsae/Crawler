import pytest
import sys
sys.path.append('src')
from utility import *
import os

def read_file(filename):
    return open(f'test/utility/test-data/{filename}', 'r').read()

testdata_parse_allow = [
    ('vg_robots.txt', []),
    ('reddit_robots.txt', ['/', '/sitemaps/*.xml', '/posts/*']),
    ('test_robots.txt', ['/pleasebethere'])
    ]
@pytest.mark.parametrize("file, expected", testdata_parse_allow)
def test_parse_allow(file, expected):
    data = read_file(file)
    rp = RobotParser(data)
    rp.parse()
    assert(rp.allow) == expected

testdata_parse_disallow = [
    ('vg_robots.txt', ['/tegneserier/salesposter', '/poll']),
    ('reddit_robots.txt', ['/r/*/comments/*/*/c*', '/r/*/user/', '/gold?', '/static/button/button1.js', '/static/button/button1.html', '/CAPS']),
    ('test_robots.txt', ['?please=123'])
    ]
@pytest.mark.parametrize("file, expected", testdata_parse_disallow)
def test_parse_disallow(file, expected):
    data = read_file(file)
    rp = RobotParser(data)
    rp.parse()
    assert(rp.disallow) == expected

testdata_parse_crawl_delay = [
    ('vg_robots.txt', 0),
    ('reddit_robots.txt', 120),
    ('test_robots.txt', 400)
    ]
@pytest.mark.parametrize("file, expected", testdata_parse_crawl_delay)
def test_parse_disallow(file, expected):
    data = read_file(file)
    rp = RobotParser(data)
    rp.parse()
    assert(rp.crawl_delay) == expected