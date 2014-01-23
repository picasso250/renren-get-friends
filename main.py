

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

def process_content(content, master_uid):
    pass
    info_list = parser.get_friend_list(content)
    # print info
    for info in info_list:
        pass
        db.insert_on_duplicate('student', info)

    for uid in [x['uid'] for x in info_list]:
        pass
        db.insert_on_duplicate('relation', {'s1': str(master_uid), 's2': str(uid)})


def fetch_person(uid):

    # fetch first
    content = fetch.get_text('/GetFriendList.do', {'curpage': '0', 'id': str(uid)})
    fetch.set_cache('a', content)
    content = fetch.get_cache('a')
    # print content
    process_content(content, uid)

    # get page
    count = parser.get_page_count(content)
    # count = 0
    print 'total',count
    if count >= 1:
        # fetch every
        for i in xrange(1,count):
            pass
            content = fetch.get_text('/GetFriendList.do', {'curpage': str(i), 'id': str(uid)})
            process_content(content, uid)
            
        pass


fetch_person('228417767')
