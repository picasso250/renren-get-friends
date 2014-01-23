

import os, re
import httplib, urllib
import fetch
import parser

# t = fetch.get_text('/GetFriendList.do', {'curpage': '0', 'id': '228417767'})
# fetch.set_cache('a', t)
t = fetch.get_cache('a')
print t

info = parser.get_friend_list(t)
print info
# parser.get_page_count(t)
# fetch first
# get page
# fetch every
