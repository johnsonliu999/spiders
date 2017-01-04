import urllib2
import urllib
import cookielib
import execjs


'''
1. visit img_url get set-cookie
2. visit login_url post form
'''

login_url = 'http://210.42.121.132/servlet/Login'
login_req = urllib2.Request(login_url)
img_url = 'http://210.42.121.132/servlet/GenImg'
img_req = urllib2.Request(img_url)

headers = [("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0"),
           ("Connection","keep-alive")]

cookie_obj = cookielib.MozillaCookieJar()
handler = urllib2.HTTPCookieProcessor(cookie_obj)
opener = urllib2.build_opener(handler)
opener.addheaders = headers

# visit img_url, get cookie & store verification
response = opener.open(img_req)
response
f = open('xdvfb.jpg', 'wb')
f.write(response.read())
f.close()

#

md5 = execjs.compile(open('md5.js').read())

id = '2013302580066'
pwd = '19940916'
encryptedPwd = md5.call('getEncryptedPwd', pwd)
print type(encryptedPwd)
xdvfb = raw_input('xdvfb:')

form = {'id':id,
        'pwd':encryptedPwd,
        'xdvfb':xdvfb}

postdata = urllib.urlencode(form)

response = opener.open(login_url, postdata)
f = open('test.html', 'w')
f.write(response.read())
f.close()



