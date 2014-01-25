# -*- coding: utf-8 -*-


import os, re
import httplib, urllib
import fetch
import parser
import db

def get_or_create_school(name):
    sid = db.find_one_val('select id from school where name=%s', [name])
    if sid is not None:
        return sid
    else:
        print 'insert'
        return db.insert('school', {'name': name})

def get_info(uid):
    t = fetch.get_url('www.renren.com', '/'+str(uid)+'/profile', {'v': 'info_timeline'})
    info = parser.get_info(t)
    for x in info:
        print x, info[x]
    print
    return info

def save_school_info(uid, info):
    info['uid'] = uid
    db.insert_on_duplicate('school', info)
    pass
def save_info(uid, info):

    # uni
    if info.has_key('uni_id'):
        print 'no key uni_id'
        info['uni_id'] = get_or_create_school(info['uni'])
        del info['uni']

    # college
    if info.has_key('college_id'):
        print 'no key college_id'
        info['college_id'] = get_or_create_school(info['college'])
        del info['college']

    # school
    if info.has_key('high_school_id'):
        print 'no key high_school_id'
        info['high_school_id'] = get_or_create_school(info['high_scool'])
        del info['high_scool']

    info['uid'] = uid
    info['has_visit_info'] = 1

    db.insert_on_duplicate('student', info)

uid = '21441'
info = get_info(uid)


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
