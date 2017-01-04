'''
1. visit douban.com get cookie
*2. may need to get captcha img
2. post {source, form_email, form_password} to login url
4. check return page see if
'''

import urllib2
import cookielib
import urllib
import re

# visit douban and get cookie
headers = [('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0')]

cookie_obj = cookielib.LWPCookieJar()
handler = urllib2.HTTPCookieProcessor(cookie_obj)
opener = urllib2.build_opener(handler)
opener.addheaders = headers

douban_url = 'https://www.douban.com'
response = opener.open(douban_url)

# try find captcha
captcha = ''
captcha_id = ''
html = response.read()
pattern = r'src="(.*?id=(.*?)&.*?)" alt="captcha"'
cap = re.findall(pattern, html)
if cap:
    captcha_url = cap[0][0]
    captcha_id = cap[0][1]
    print captcha_url, captcha_id
    urllib.urlretrieve(captcha_url, 'captcha.jpg')
    captcha = raw_input('Input captcha:')

# visit login, post data
login_url = 'https://www.douban.com/accounts/login'

source = 'index_nav'
form_email = '452977491@qq.com'
form_password = 'qq452977491'

form = {'source' : source,
        'form_email' : form_email,
        'form_password' : form_password}

if captcha:
    form['captcha-id'] = captcha_id
    form['captcha-solution'] = captcha

post_data = urllib.urlencode(form)

response = opener.open(login_url, post_data)
if cookie_obj.as_lwp_str().find('dbcl2') != -1:
    print 'Login succeed'
else:
    print 'Login Failed'