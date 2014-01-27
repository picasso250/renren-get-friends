# -*- coding: utf-8 -*-

import os, re
import httplib, urllib
import fetch
import santi_parser
import db

# content = fetch.get_url('bbs.hupu.com', '/7349086.html', {}, 'gbk')
# print content

def get_save_page(page_num):
    print page_num
    url = '/7349086';
    if page_num != 1:
        url += '-'+str(page_num)
    url += '.html'
    content = fetch.get_url('bbs.hupu.com', url, {}, 'gbk')
    scene_list = santi_parser.get_scene_list(content)
    for scene in scene_list:
        scene['text'] = scene['text'].strip()
        m = re.match('(\d+)([a-z]?)', scene['number'])
        scene['number'] = (m.group(1))
        if m.group(2) is not None:
            scene['number_extra'] = m.group(2)
        db.insert('scene', scene)
    print 'ok'

for i in xrange(1,4):
    get_save_page(i)
