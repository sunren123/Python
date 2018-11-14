import requests

session =requests.session()

post_url = "http://www.renren.com/PLogin.do"
post_data = {"email":"462227979@qq.com","password":"qq5897008"}
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}

session.post(post_url,data=post_data,headers=headers)

r = session.get("http://www.renren.com/337981313/profile")
f = open("renren.html","w",encoding="utf-8")
f.write(r.content.decode())
f.close()