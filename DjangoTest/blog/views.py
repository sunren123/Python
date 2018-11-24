from datetime import date
from django.shortcuts import render,redirect
from django.http import HttpResponse

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
    b.bpub_date =date(1990,1,1)
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
    return render(request,"login.html")




def login_check(request):
    username = request.GET.get('username')
    password = request.GET.get('password')

    if username == 'sunren' and password == '123':
        return HttpResponse("登录成功")
    else:
        return HttpResponse("登录失败")





def set_session(request):
    request.session["username"] = "sunren"
    request.session["age"] = 18
    return  HttpResponse("设置session")

def get_session(request):
    username = request.session["username"]
    age = request.session["age"]
    return HttpResponse(username+":"+str(age))



