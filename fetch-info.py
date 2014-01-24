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
    pass
    t = fetch.get_url('www.renren.com', '/'+uid+'/profile', {'v': 'info_timeline'})
    info = parser.get_info(t)
    # for x in info:
    #     print x, info[x]
    # print
    return info

def save_info(uid, info):
    pass
    # uni
    info['uni_id'] = get_or_create_school(info['uni'])
    del info['uni']

    # college
    info['uni_id'] = get_or_create_school(info['college'])
    del info['college']

    # school
    info['uni_id'] = get_or_create_school(info['high_scool'])
    del info['high_scool']

    info['uid'] = uid
    info['has_visit_info'] = 1

    db.insert_on_duplicate('student', info)

uid = '146539724'
info = get_info(uid)
save_info(uid, info)
