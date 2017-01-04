import urllib2
import pprint
import cookielib
import urllib
import json
import re

headers = []

with open("headers", 'r') as f:
    for line in f.readlines():
        key, value = line.split(': ',1)
        value = value.strip('\n')
        headers.append((key, value))

cookie_obj = cookielib.LWPCookieJar()
handler = urllib2.HTTPCookieProcessor(cookie_obj)
opener = urllib2.build_opener(handler)
opener.addheaders = headers

url = 'https://www.zhihu.com/node/TopicsPlazzaListV2'

form = {'method':'next',
        'params':'{"topic_id":253,"offset":0,"hash_id":"6f14dd9bd7e39186173fc8589aa7cb11"}'}

post_data = urllib.urlencode(form)

response = opener.open(url, post_data)
content = response.read()

j = json.loads(content)
records = {}
pattern = r'alt="(.*?)".*?<p>(.*?)</p>'
# pattern = '<p>(.*?)</p>'
re_obj = re.compile(pattern, re.DOTALL)
for item in j['msg']:
    # print item
    record = re_obj.findall(item)[0]
    records[record[0]] = record[1]

pprint.pprint(records)