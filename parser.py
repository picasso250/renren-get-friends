import os, re
import httplib, urllib

import sys
reload(sys)
sys.setdefaultencoding('utf8')

from pyquery import PyQuery as pq
from lxml import etree
import urllib
from urlparse import urlparse

def get_friend_list(content):
    d = pq(content)
    li_list = d('#friendListCon > li')
    for li in li_list:
        img = li.find('p').find('a').find('img')
        avatar = img.attrib['src']
        print 'avatar:', avatar
        a = li.find('div').find('dl').find('dd').find('a')
        name = a.text
        print 'name:', name
        url = a.attrib['href']
        m = re.search('id=(\d+)', url)
        uid = m.group(1)
        print 'uid:', uid
        return {
            avatar: avatar,
            name: name,
            uid: uid,
        }
        # todo get city or school
        # todo save to mysql

def get_page_count(content):
    d = pq(content)
    a_list = d('#topPage a')
    querys = [urlparse(a.attrib['href']).query for a in a_list]
    l = []
    for q in querys:
        d = dict([x.split("=") for x in q.split("&")])
        l.append(int(d['curpage']))
    return max(l)
