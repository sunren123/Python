import requests

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36","Cookie":"anonymid=joe3zdpuan84k9; depovince=HUB; _r01_=1; ick_login=ce3cfc29-7c51-423f-b5fb-5406d3fbdcd1; _de=95A6111A8371EB2AE2A69D838E8B6F33696BF75400CE19CC; ap=337981313; first_login_flag=1; ln_uact=462227979@qq.com; ln_hurl=http://hdn.xnimg.cn/photos/hdn421/20100912/1455/h_main_W0xI_54b20001c43a2f75.jpg; id=337981313; loginfrom=syshome; __utma=151146938.2066697688.1542015202.1542015202.1542015202.1; __utmc=151146938; __utmz=151146938.1542015202.1.1.utmcsr=renren.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmb=151146938.7.10.1542015202; ick=a85a31aa-530b-421f-80b0-42e18e457a67; jebecookies=70bd5ed0-d78b-435f-9c60-6c98e904a576|||||; p=a59b716d7085081da1fd6f83b3a3c1193; t=84c44231f0631ddba551c91e1c98d2683; societyguester=84c44231f0631ddba551c91e1c98d2683; xnsid=f8b6e236; ch_id=10016; wpsid=15231411099754; wp_fold=0"}


url ="http://www.renren.com/337981313/profile"


r=requests.get(url,headers=headers)
f = open("renren2.html","w",encoding="utf-8")
f.write(r.content.decode())
f.close()