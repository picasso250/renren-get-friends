

import os, re
import httplib, urllib
import fetch
import parser
import db

# t = fetch.get_text('/GetFriendList.do', {'curpage': '0', 'id': '228417767'})
# fetch.set_cache('a', t)
# t = fetch.get_cache('a')
# print t


# info = parser.get_friend_list(t)
# print info
# parser.get_page_count(t)
# fetch first
# get page
# fetch every
# db.insert_on_duplicate('relation', {'s1': 1, 's2': 2})

def process_content(content):
    pass
    info = parser.get_friend_list(content)
    # print info
    db.insert_on_duplicate('student', info)

def fetch_person(uid):

    # fetch first
    content = fetch.get_text('/GetFriendList.do', {'curpage': '0', 'id': str(uid)})
    fetch.set_cache('a', content)
    content = fetch.get_cache('a')
    # print content
    process_content(content)

    # get page
    count = parser.get_page_count(content)
    print 'total',count
    if count >= 1:
        # fetch every
        for i in xrange(1,count):
            pass
            content = fetch.get_text('/GetFriendList.do', {'curpage': str(i), 'id': str(uid)})
            process_content(content)
            
        pass

    # db.insert_on_duplicate('relation', {'s1': 1, 's2': 2})

fetch_person('228417767')
