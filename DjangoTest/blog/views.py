from datetime import date
from django.shortcuts import render,redirect
from django.http import HttpResponse,response

from blog.models import BookInfo


from PIL import Image, ImageDraw, ImageFont
from django.utils.six import BytesIO


# Create your views here.


def index(request):
    #获取浏览器的ip地址
    user_ip=request.META['REMOTE_ADDR']
    print(user_ip)
    #查询所有的图书信息
    books= BookInfo.objects.all()
    #视图配置
    return render(request,"index.html",{"books":books},user_ip)


def create(request):
    #添加一本图书
    b = BookInfo()
    b.btitle ="流星蝴蝶剑"
    # b.bpub_date =date(1990,1,1)
    #保存数据库
    b.save()
    #返回应答
    return redirect("/index")



def delete(request, bid):
    #删除点击的图书
    book =BookInfo.objects.get(id=bid)
    book.delete()
    return redirect("/index")





def login(request):
    #判断用户是否登录
    if request.session.has_key("islogin"):
        return redirect("/index")

    else:
        #用户登录
        #获取cookie
        if "username" in request.COOKIES:
            username= request.COOKIES["username"]
        else:
            username=""
        return render(request,"login.html",{"username":username})




def login_check(request):
    username = request.POST.get('username')
    password = request.POST.get('pwd')
    remember = request.POST.get('remember')
    if username == 'sunren' and password == '123':
        # 用户名正确，跳转到首页
        response = redirect("/index")
        #判断是否需要记住用户名
        if remember == "on":
            #设置cookie 过期时间
            response.set_cookie("username",username,max_age=7*24*3600)

        #记住用户登录状态
        request.session["islogin"] = True
        #记住登录的用户名
        request.session["username"] = username

        return response
    else:
        return redirect("/login")


#登录判断装饰器
def login_required(view_func):
    #登录判断装饰器
    def wrapper(request, *view_args, **view_kwargs):
        if request.session.has_key("islogin"):
            #用户已经登录
            return view_func(request, view_args, view_kwargs)
        else:
            #用户没有登录
            return redirect("/login")
    return wrapper


@login_required
def change_pwd(request):
    #用户登录是否
    # if not request.session.has_key("islogin"):
    #     return redirect("/login")
    return render(request,'change_pwd.html')

@login_required
def change_pwd_action(request):
    #获取心密码
    pwd = request.POST.get('pwd')
    #获取用户名
    username =request.session.get("username")
    return HttpResponse("%s新密码为：%s"% (username,pwd))


