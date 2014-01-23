
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
        'Cookie': 'anonymid=hpxwsygtz6u2gu; _r01_=1; JSESSIONID=abcdgJ9l1JeQqhUbROsnu; ick_login=f47bf458-d027-499b-a01a-3ffed2a24688; XNESSESSIONID=af90d1e7d217; ick=21fc8c10-f211-40d5-a43d-db1c536d5a0a; _de=6B3F68A3B98BADDE348942222129E7F8FA025FA9A94C8260; depovince=GW; jebecookies=fcf969e9-45a4-4dee-82a8-c2f7c105115a|||||; p=21bb50850754cafa0695f6875b12b7ec7; ap=228417767; t=a940bff63e77655037972b1ab99238987; societyguester=a940bff63e77655037972b1ab99238987; id=228417767; xnsid=412ce95b; loginfrom=null; feedType=228417767_hot',
        'Accept-Language': 'zh-CN,zh;q=0.8'
    }
    for key in extra:
        headers[key] = extra[key]
    return headers

def get_text(url, data = {}):
    # http://friend.renren.com/GetFriendList.do?curpage=1&id=228417767
    data = urllib.urlencode(data)
    conn = get_renren_conn()
    print url+'?'+data
    conn.request("GET", url+'?'+data, None, get_headers())
    response = conn.getresponse()
    content = response.read()
    set_cache('cache', content)
    content = get_cache('cache')
    return content

def get_cache(name):
    filename = name+'.cache'
    if not os.path.exists(filename):
        print 'no file', filename
        return None
    f = open(filename, 'r')
    c = f.read()
    f.close()
    return c

def set_cache(name, content):
    filename = name+'.cache'
    f = open(filename, 'w')
    c = f.write(content)
    f.close()
