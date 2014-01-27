# -*- coding: utf-8 -*-

import os, re
import httplib, urllib
import fetch
import santi_parser
import db
from urlparse import urlparse

images = db.find_many_val('select img from scene')
print images

# url = 'http://i1.hoopchina.com.cn/u/1311/23/027/33027/5dde67c8.jpg'
def fetch_save_picture(url):
    o = urlparse(url)
    path = o.path
    content = fetch.get_url(o.hostname, path)
    # ff = open('get_url.cache', 'r')
    # content = ff.read()
    # ff.close()
    path = re.sub('^/', '', path)
    path = re.sub('/', '-', path)
    f = open('images/'+path, 'w');
    f.write(content);
    f.close()

for url in images:
    fetch_save_picture(url)
