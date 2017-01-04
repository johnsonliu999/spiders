import cookielib
import urllib2
import urllib
import time
import execjs
from execjs import ProgramError

modulus = '00ac634ef2e3b077ef921aafab6570023615f2f19942dc25a58cd706908738982be2dad9918d042ae18d5e3a007c92bc93e01675a2a8384c83127ae450772a50cd450d1ac59bee42d740106586436109f46a6b532ad9b124e980dce50c376a8e21f9abe2bf50f87381ce96e6df8ae7c29e52bf0b843936f3e4afc7d54f086edd09'
exponent = '010001'

security = execjs.compile(open('security.js').read())
try:
    pwd = security.call('getPwd', '160018')
    print pwd
except ProgramError, e:
    print e.message
    print e.args
except TypeError, e:
    print e.message
    print e.args

#print pwd


header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',}

url = "http://202.114.74.199/login.action?&t=" + str(int(time.time()))
print(url)


cookie_obj = cookielib.MozillaCookieJar()
login_url = "http://202.114.74.199/login.action"
view_url = "http://202.114.74.199/view/index.action"

login_req = urllib2.Request(login_url)
login_req.add_header('Referer','http://202.114.74.199/login.action?backurl=http://202.114.74.199/view/index.action')

handler = urllib2.HTTPCookieProcessor(cookie_obj)
opener = urllib2.build_opener(handler)
opener.addheaders = [(key, value) for key, value in header.items()]

postdata = dict(username='2013302580066', password='160018',
                encodedPassword=pwd, backurl=view_url)
postdata = urllib.urlencode(postdata)

response = opener.open(login_req, postdata)

f = open('test.html', 'w')
f.write(response.read())
f.close()





