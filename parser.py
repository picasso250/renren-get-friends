import os, re
import httplib, urllib

import sys
reload(sys)
sys.setdefaultencoding('utf8')

from pyquery import PyQuery as pq
from lxml import etree
import urllib

def get_friend_list(content):
    pass
    d = pq(content)
    # print d
    li_list = d('#friendListCon > li')
    # li_list = ol.find('li')
    for li in li_list:
        pass
        # a_list = li.find('a')
        # if a_list is not None:
        #     for a in a_list:
        #         print a.text
        # print dir(li)
        print '------------------'
        img = li.find('p').find('a').find('img')
        avatar = img.attrib['src']
        print 'avatar', avatar
        a = li.find('div').find('dl').find('dd').find('a')
        name = a.text
        print 'name', name
        url = a.attrib['href']
        m = re.search('id=(\d+)', url)
        uid = m.group(1)
        print 'uid', uid
        # todo get city or school
        # todo page
        # todo can next page?
        # todo save to mysql

