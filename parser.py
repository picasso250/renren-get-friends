# -*- coding: utf-8 -*-

import os, re
import httplib, urllib
import json

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
    print len(a_list)
    if len(a_list) == 0:
        return 0
    querys = [urlparse(a.attrib['href']).query for a in a_list]
    l = []
    for q in querys:
        d = dict([x.split("=") for x in q.split("&")])
        l.append(int(d['curpage']))
    if len(l) == 0:
        print 'err: l is empty'
        # todo log
    return max(l)

def extract_digits(string):
    m = re.search('^\d+', string)
    return m.group(0)

def get_info(content):
    if content.find(u'只公开了一部分信息') != -1:
        print '只公开了一部分信息'
        return {'is_private': 1}

    if content.find(u'The URL has moved') != -1:
        print 'captcha'
        return False

    d = pq(content)
    data = {}
    # todo frd count
    frd = d('#allFrdGallery')
    if len(frd) != 0:
        print 'allFrdGallery'
        data['is_private'] = 1
        m = re.search(r'\d+', frd.find('h3').text())
        data['friends_count'] = m.group(0)
        li_list = frd.find('ul').find('li')
        frd_list = []
        for li in li_list:
            dd = pq(li)
            m = re.search(r'id=(\d+)', dd('.avatar').attr('href'))
            uid = m.group(1)
            name = dd('.name').text()
            info = dd('.network').text()
            frd_list.append({
                'uid': uid,
                'name': name,
                'public_info': info
                })
        data['frd_list'] = frd_list
        return data

    dl_list = d('#educationInfo dl')
    educationInfo = []
    for dl in dl_list:
        dt = dl.find('dt')
        dd = pq(dl)
        educationInfo.append({
            'type': dt.text,
            'info': ' - '.join([a.text for a in dd('a')])
            })
    if len(educationInfo) > 0:
        pass
        data['educationInfo'] = educationInfo

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

    dl_list = d('#workInfo dl')
    workInfo = {}
    workInfo_list = []
    for dl in dl_list:
        dt = dl.find('dt')
        dd = pq(dl)
        if dt.text == '公司':
            workInfo['name'] = dd('dd').text()
        if dt.text == '时间':
            workInfo['time_range'] = dd('dd').text()
            workInfo_list.append(workInfo)
            workInfo = {}
    if len(workInfo_list) > 0:
        pass
        data['workInfo'] = workInfo_list


    dl_list = d('#basicInfo dl')
    field_map = {
        '生日': 'birthday',
        '家乡': 'hometown',
        '性别': 'gender',
    }
    for dl in dl_list:
        dt = dl.find('dt')
        dd = pq(dl)
        if not field_map.has_key(dt.text.encode('utf8')):
            print 'no key', dt.text
        data[field_map.get(dt.text.encode('utf8'))] = dd('dd').text()

    return data
