from datetime import date
from django.shortcuts import render,redirect
from django.http import HttpResponse,response

from blog.models import BookInfo


# Create your views here.


def index(request):
    #查询所有的图书信息
    books= BookInfo.objects.all()
    #视图配置
    return render(request,"index.html",{"books":books})


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






from PIL import Image, ImageDraw, ImageFont
from django.utils.six import BytesIO
...
def verify_code(request):
    #引入随机函数模块
    import random
    #定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100), random.randrange(
        20, 100), 255)
    width = 100
    height = 25
    #创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    #创建画笔对象
    draw = ImageDraw.Draw(im)
    #调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    #定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    #随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    #构造字体对象，ubuntu的字体路径为“/usr/share/fonts/truetype/freefont”
    font = ImageFont.truetype('FreeMono.ttf', 23)
    #构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    #绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    #释放画笔
    del draw
    #存入session，用于做进一步验证
    request.session['verifycode'] = rand_str
    #内存文件操作
    buf = BytesIO()
    #将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    #将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')