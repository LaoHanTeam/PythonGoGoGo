#coding:utf-8

import urllib2,urllib,cookielib,json

username = ""
password = ""

class sign(object):
    username = ''
    password = ''

    #登录显示页面
    indexUrl = "https://www.kuaipan.cn/account_login.htm"

    #登录的form表单url
    loginurl = "https://www.kuaipan.cn/index.php?ac=account&op=login"

    #签到url
    signUrl = "http://www.kuaipan.cn/index.php?ac=common&op=usersign"

    def __init__(self ,username,password):
        self.username = username
        self.password = password

    def login(self):
        cj = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        urllib2.install_opener(opener)
        print "打开登录页面"
        try:
            urllib2.urlopen(self.indexUrl)
            post_data = {'username':self.username,'userpwd':self.password,'isajax':'yes'}
            req = urllib2.Request(self.loginurl,urllib.urlencode(post_data))
        except Exception , e:
            print "网络连接错误"
            return False
        print "登录成功，准备签到！"

        response = urllib2.urlopen(req)
        login = response.read()
        print login
        return login

    def sign(self):
        response = urllib2.urlopen(self.signUrl)
        sign = response.read()
        #print sign
        l = json.load(sign)
        if(l and l['state']) or (l and 0 == l['state'] and l['increase']*1 == 0 and l['monthtask'].M900 == 900):
            print "恭喜你签到成功"

            k = l['increase']*1
            m = l['rewardsize']*1

            if(k == 0 and l['monthtask'].M900 == 900):
                print "本月签到积分已领取完成"
            else:
                print "签到积分奖励：%s" %(k)
            if m == 0:
                print "手气不好了"
            else :
                print "签到奖励空间：%s" %(m)

        else:
            if(l['state'] == -102):
                print "今天你已经签到过了"
            else :
                print "签到失败，遇到网络错误"
        return sign


if __name__ == "__main__":
    sign = sign(username , password)
    if sign.login():
        sign.sign()
