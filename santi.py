# -*- coding: utf-8 -*-

import os, re
import httplib, urllib
import fetch
import santi_parser
import db

content = fetch.get_url('bbs.hupu.com', '/7349086.html', {}, 'gbk')
# print content

scene_list = santi_parser.get_scene_list(content)
for scene in scene_list:
    scene['text'] = scene['text'].strip()
    m = re.match('(\d+)([a-z]?)', scene['number'])
    scene['number'] = int(m.group(1))
    if m.group(2) is not None:
        scene['number_extra'] = m.group(2)
    db.insert('scene', scene)
print 'ok'
