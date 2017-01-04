'''
1. visit zhihu.com to get cookie and extract xsrf
2. visit chaptcha
3. visit https://www.zhihu.com/login/email
    and post _xsrf, pwd, captcha and email
4. from response get json
'''

'''
only email login
'''

import cookielib
import urllib2
import urllib
import time
import re

headers = [('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0')]

# visit index; set cookie; extract xsrf
'''
1. prepare cookie object
2. use cookie build handler
3. build opener use handler and add header
4. open request
'''
cookie_obj = cookielib.LWPCookieJar()
handler = urllib2.HTTPCookieProcessor(cookie_obj)
opener = urllib2.build_opener(handler)
opener.addheaders = headers

index_url = 'https://www.zhihu.com'
response = opener.open(index_url)
set_cookie = response.info()['Set-Cookie']
pattern = r'_xsrf=(.*?);'
xsrf = re.findall(pattern, set_cookie)[0]

# get chaptcha
captcha_url = 'http://www.zhihu.com/captcha.gif?r=' + str(int(time.time()*1000)) + '&type=login'
print captcha_url
response = opener.open(captcha_url)
f = open('chaptcha.gif', 'wb')
f.write(response.read())
f.close()

# visit login and post data
captchar = raw_input('Input chaptcha:')

form = {'_xsrf' : xsrf,
        'password' : 'qq452977491',
        'email' : '452977491@qq.com',
        'captcha' : captchar}
post_data = urllib.urlencode(form)
print post_data

login_url = 'https://www.zhihu.com/login/email'
response = opener.open(login_url, post_data)
print response.read().decode('unicode-escape')