# import MySQLdb

# try:
#     conn=MySQLdb.connect(host='localhost',user='root',passwd='',db='renren_data',port=3306)
#     cur=conn.cursor()
#     cur.execute('select * from test')
#     a = cur.fetchmany()
#     print a[0][0]
#     cur.close()
#     conn.close()
# except MySQLdb.Error,e:
#      print "Mysql Error %d: %s" % (e.args[0], e.args[1])

import os, re
import httplib, urllib

def get_renren_conn():
    return httplib.HTTPConnection("friend.renren.com")

def get_headers(extra = {}):
    headers = {
        'Connection': 'keep-alive',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/28.0.1500.71 Chrome/28.0.1500.71 Safari/537.36',
        'Referer': 'http://friend.renren.com/GetFriendList.do?curpage=1&id=228417767',
        'Cookie': 'anonymid=hqjjjuvj-kvzho9; depovince=GW; jebecookies=f85dd420-a520-46c6-9607-a804123918ed|||||; _r01_=1; ick_login=2bc9e132-b666-4b4f-b245-47598cbb0fb6; _de=6B3F68A3B98BADDE348942222129E7F8FA025FA9A94C8260; p=21bb50850754cafa0695f6875b12b7ec7; t=224616965b77eb308957b367d744f22a7; societyguester=224616965b77eb308957b367d744f22a7; id=228417767; xnsid=5f669cf1; JSESSIONID=abck19ccQAnwm5ArAMGou; jebe_key=d7fa9251-97f7-4a95-a5d4-15ffdfa34a2b%7Cee432b942a06fe5bbfda0828a72706ec%7C1389968865431%7C1; loginfrom=null; XNESSESSIONID=35bda184f953',
        'Accept-Language': 'zh-CN,zh;q=0.8'
    }
    for key in extra:
        headers[key] = extra[key]
    return headers

def get_text(url, data = {}):
    # http://friend.renren.com/GetFriendList.do?curpage=1&id=228417767
    data = urllib.urlencode(data)
    conn = get_renren_conn()
    conn.request("GET", url+'?'+data, None, get_headers())
    response = conn.getresponse()
    return response.read()

def get_cache(name):
    filename = '/tmp/'+name+'.cache'
    if not os.path.exists(filename):
        print 'no file', filename
        return None
    f = open(filename, 'r')
    c = f.read()
    f.close()
    return c

def set_cache(name, content):
    filename = '/tmp/'+name+'.cache'
    f = open(filename, 'w')
    c = f.write(content)
    f.close()

# t = get_text('/GetFriendList.do', {'curpage': '0', 'id': '228417767'})
# set_cache('a', t)
t = get_cache('a')
# print t
r = re.compile(r'<ol id="friendListCon">.+?</ol>', re.S)
m = r.search(t)
ol = m.group(0)
# print ol
set_cache('ol', ol)

import sys
reload(sys)
sys.setdefaultencoding('utf8')


from pyquery import PyQuery as pq
from lxml import etree
import urllib
d = pq(t)
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
    img = li.find('p').find('a').find('img')
    avatar = img.attrib['src']
    print 'avatar', avatar
    # print li.find('p.avatar img')
    dd_list = li.find('dd')
    if dd_list is None:
        continue
    for dd in dd_list:
        pass
        if dd.text is not None:
            school = dd.text.strip()
            print 'school', school
    # print dir(li)
