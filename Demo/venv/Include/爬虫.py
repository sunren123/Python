import re
import requests


#
url= "http://www.xiaohuar.com/mm/"
#返回网页代码
wb_data =requests.get(url)
# print(wb_data)

#解析网页
wb_data.encoding='gbk'
res =re.findall(r'src="(.*?.jpg)"',wb_data.text)
# print(res)

# 保存数据
num =0
for i in res:
    print(i)
    if i.startswith('/d'):
        i = 'http://www.xiaohuar.com'+i
        print(i)

        b =requests.get(i)
                                                                         #wb 二进制文件
        with open(r'C:\Users\Administrator\Desktop\tupian\%s.jpg'% num,'wb')as f:
            f.write(b.content)
            num =num +1
            print('第{}张图片下载'.format(num))