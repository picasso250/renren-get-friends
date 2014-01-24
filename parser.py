# -*- coding: utf-8 -*-

import os, re
import httplib, urllib

import sys
reload(sys)
sys.setdefaultencoding('utf8')

from pyquery import PyQuery as pq
from lxml import etree
import urllib
from urlparse import urlparse

def is_private(content):
    return content.find(u'由于对方设置隐私保护，您没有权限查看此内容') != -1

def get_friend_list(content):
    if is_private(content):
        return []
    d = pq(content)
    li_list = d('#friendListCon > li')
    l = []
    for li in li_list:
        div = li.find('div')
        if div is None:
            # todo log it
            print 'div is None'
            continue
        dl = div.find('dl')
        if dl is None:
            print 'dl is None'
        a = dl.find('dd').find('a')
        name = a.text
        url = a.attrib['href']
        m = re.search('id=(\d+)', url)
        uid = m.group(1)
        print 'uid:', uid,
        print 'name:', name
        data = {
            'name': name,
            'uid': uid,
        }
        img = li.find('p').find('a').find('img')
        if img is not None:
            pass
            avatar = img.attrib['src']
            data['avatar'] = avatar
        else:
            print 'error img'

        l.append(data)
        # todo get city or school
    return l

def get_page_count(content):
    if is_private(content):
        return -1
    d = pq(content)
    a_list = d('#topPage a')
    querys = [urlparse(a.attrib['href']).query for a in a_list]
    l = []
    for q in querys:
        d = dict([x.split("=") for x in q.split("&")])
        l.append(int(d['curpage']))
    return max(l)

def extract_digits(string):
    m = re.search('^\d+', string)
    return m.group(0)

def get_info(content):
    data = {}
    d = pq(content)
    dl_list = d('#educationInfo dl')
    for dl in dl_list:
        dt = dl.find('dt')
        dd = pq(dl)
        if dt.text == '大学':
            data['uni'], college_year, data['college'] = [a.text for a in dd('a')]
            data['college_year'] = extract_digits(college_year)
        if dt.text == '高中':
            data['high_scool'], high_school_year, _ = [a.text for a in dd('a')]
            data['high_school_year'] = extract_digits(high_school_year)

    data['is_in_love'] = d('.love-infobox p').text()

    dl_list = d('#contactInfo dl')
    for dl in dl_list:
        dt = dl.find('dt')
        dd = pq(dl)
        if dt.text == '手机':
            data['mobile'] = dl.find('dd').text
        if dt.text == 'MSN':
            data['msn'] = dl.find('dd').text
        if dt.text == '个人网站':
            data['website'] = dd('dd a').text()

    return data
