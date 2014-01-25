# -*- coding: utf-8 -*-


import os, re
import httplib, urllib
import fetch
import parser
import db
import json

def get_or_create_school(name):
    sid = db.find_one_val('select id from school where name=%s', [name])
    if sid is not None:
        return sid
    else:
        print 'insert'
        return db.insert('school', {'name': name})

def get_info(uid):
    content = fetch.get_url('www.renren.com', '/'+str(uid)+'/profile', {'v': 'info_timeline'})
    info = parser.get_info(content)
    return info

def save_school_info(uid, info):
    info['uid'] = uid
    info['has_visit_info'] = 1
    db.insert_on_duplicate('school', info)

def save_work_info(uid, info_list):
    for x in info_list:
        info['uid'] = uid
        info['has_visit_info'] = 1
        db.insert_on_duplicate('company', info)

def save_basic_info(uid, info):
    info['uid'] = uid
    info['has_visit_info'] = 1
    db.insert_on_duplicate('student', info)

uid = '21441'
print 'get_info'
info = get_info(uid)
print 'info', json.dumps(info, encoding="UTF-8", ensure_ascii=False)


while False:
    uid = db.find_one_val('select uid from student where has_visit_info=0 limit 1')
    print uid
    if uid:
        print '--------------------',uid
        info = get_info(uid)
        save_info(uid, info)
        # break
    else:
        break

    pass
