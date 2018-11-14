# a=[1,2,3,4,5,6,7,8]
# for i in a:
#     print("执行第{}个".format(i))
#     print("*"*15)

# my_list =range(18)
# for i in my_list:
#     print("当前是第{}".format(i))
#     print("*"*10)

# a =1
# sum= 0
# while a<=100:
#      if a%2==0:
#         sum = sum+a
#      a =a + 1
#
#      print(sum)

# def get_volume(x):  #获取正方形的体积
#    vs =x*x*x
#    return vs
#
# v1 =get_volume(20)
# v2 =get_volume(21)
# print(v2-v1)

year = input("请输入年份：")

def get_year(year):
    if year%4==0 and year%100!=0:
       print("{}是闰年".format(year))
    elif year%400==0:
       print("{}是闰年".format(year))
    else:
       print("{}不是闰年".format(year))





