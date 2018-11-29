from django.shortcuts import render

# Create your views here.
from blog.models import PicTest,AreaInfo

# show_upload
def show_upload(request):
    return render(request, "upload_pic.html")


def upload_handle(request):
    #上传图片处理

    #1.获取上传的文件的处理对象
    pic=request.FILES["pic"]
    #2.创建一个文件
    #3获取上传文件的内容写到文件中
    #4.在数据库保存记录
    #5.返回
from django.core.paginator import Paginator
def show_area(request,pindex):
    #分页
    #查询所有省级地区的信息
    areas=AreaInfo.objects.filter(aParent__isnull=True)
    #分页，显示10条
    paginator=Paginator(areas,10)
    # 获取第一页的内容
    #page是Page类的实例
    if pindex =="":
        pindex = 1
    else:
        pindex =int(pindex)
    page = paginator.page(pindex)

    return render(request,"show_area.html",{'page':page})



def areas(request):
    return render(request,"areas.html")