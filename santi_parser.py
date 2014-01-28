# -*- coding: utf-8 -*-

import os, re
import httplib, urllib
import json

import sys
reload(sys)
sys.setdefaultencoding('utf8')

from pyquery import PyQuery as pq
from lxml import etree
import urllib
from urlparse import urlparse

from HTMLParser import HTMLParser

class SantiParser(HTMLParser):
    def __init__(self):
        self.reset()
        self.scene_list = []
        self.scene = None
        self.is_first_line = False

    def handle_starttag(self, tag, attrs):
        # print "Encountered a start tag:", tag
        if tag == 'img':
            self.is_first_line = True
            if self.scene is not None:
                self.scene_list.append(self.scene)
            src = attrs[0][1]
            # print 'img src', src
            self.scene = {'img': src, 'number': '', 'text': ''}
            self.last_tag = tag
        if tag == 'br' and self.scene is not None:
            self.scene['text'] += '\n'

    def handle_endtag(self, tag):
        # print "Encountered an end tag :", tag
        if tag == 'td' and self.scene is not None:
            self.scene_list.append(self.scene)

    def handle_data(self, d):
        if self.scene is not None:
            # print d
            if self.is_first_line:
                # print '^^^^^^^^^^^^^^^^^^^^^'
                if re.match(r'\d+[a-z]?', d):
                    # print '====================================='
                    self.scene['number'] = d
                else:
                    self.scene = None
        if self.scene is not None and not re.match(r'\d+[a-z]?', d):
            self.scene['text'] += d
        self.is_first_line = False

    def get_scene_list(self):
        return self.scene_list

def get_scene_list(content):
    ret = []
    i = 1
    reg = re.compile(r'<td>.+?</td>', re.DOTALL)
    for m in reg.finditer(content):
        html = m.group(0)
        s = SantiParser()
        s.feed(html)
        for x in s.get_scene_list():
            x['act'] = i
            ret.append(x)
        # print 'html', html
        i += 1
    for x in ret:
        print '----------------------------'
        print x['img']
        print x['number']
        print x['text'].strip()
    return ret

if __name__ == "__main__":
    f = open('get_url.cache', 'r')
    content = f.read()
    f.close()
    s = get_scene_list(content)
    # print s
    
