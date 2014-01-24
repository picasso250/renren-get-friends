
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
        'Cookie': 'anonymid=hqjjjuvj-kvzho9; _r01_=1; JSESSIONID=abc-HF0haDFRBflfsMGou; jebe_key=d7fa9251-97f7-4a95-a5d4-15ffdfa34a2b%7Cee432b942a06fe5bbfda0828a72706ec%7C1389968865431%7C1; XNESSESSIONID=35bda184f953; depovince=GW; jebecookies=abffd128-60eb-432b-9964-0125d1bad618|||||; ick_login=2bc9e132-b666-4b4f-b245-47598cbb0fb6; _de=6B3F68A3B98BADDE348942222129E7F8FA025FA9A94C8260; p=21bb50850754cafa0695f6875b12b7ec7; ap=228417767; t=0462ee96e3c7b4085537c221eb1bbcf47; societyguester=0462ee96e3c7b4085537c221eb1bbcf47; id=228417767; xnsid=3e63f473; loginfrom=null; feedType=228417767_hot',
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
    # todo status not 200
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
