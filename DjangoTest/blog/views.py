from datetime import date
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
import time
from blog.models import BookInfo
from django.template import loader

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
    return HttpResponseRedirect("/index")



def delete(request, bid):
    #删除点击的图书
    book =BookInfo.objects.get(id=bid)
    book.delete()

    return HttpResponseRedirect("/index")