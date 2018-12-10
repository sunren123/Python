from django.shortcuts import render,redirect,HttpResponse

# Create your views here.




def index(request):
    username = request.POST.get("username")
    return render(request,"index.html",locals())


def login(request):
    #判断用户是否登录
    if request.session.has_key("islogin"):
        return redirect("/index")
    else:
        #用户登录
        #获取cookie
        if "username" in request.COOKIES:
            username = request.COOKIES["username"]
        else:
            username = ""
        return render(request , "login.html" ,{"username": username})

def login_check (request):
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


from book import models

def classes(request):
    clsaaes = models.Classes.objects.all()
    return render(request,"classes.html",locals())



def add_classes(request):
    if request.method == "GET":
        return render(request , "add_classes.html")

    elif request.method == "POST":
        title = request.POST.get("title")
        models.Classes.objects.create(titile=title)
        return redirect("/classes")


def del_classes(request):
    nid = request.GET.get("nid")
    models.Classes.objects.filter(id=nid).delete()
    return redirect("/classes")

def edit_classes(request):
    if request.method=="GET":
        nid = request.GET.get("nid")
        obj = models.Classes.objects.filter(id=nid).first()
        return render(request,"edit_classes.html",locals())
    elif request.method == "POST":
        nid = request.GET.get("nid")
        title = request.POST.get("xx")
        models.Classes.objects.filter(id=nid).update(titile=title)
        return redirect("/classes")



def get_students(request):
    stu_list = models.Student.objects.all()
    return render(request, "get_students.html", locals())


def add_students(request):
    if request.method == "GET":
        cs_list = models.Classes.objects.all()
        return render(request,"add_students.html",locals())

    elif request.method == "POST":
        name =request.POST.get("username")
        age =request.POST.get("age")
        gender =request.POST.get("gender")
        c =request.POST.get("cs")
        models.Student.objects.create(
            username=name,
            age=age,
            gender=gender,
            cs_id=c
        )
        return redirect("/get_students")



def ajax1(request):

    return render(request,"ajax.html")



def ajax2(request):
    user = request.GET.get("username")
    pwd = request.GET.get("password")
    import time
    time.sleep(5)

    return HttpResponse("我愿意")




def ajax3(request):
    v1 = request.POST.get("v1")
    v2 = request.POST.get("v2")
    try:
        v3 = int(v1) +int(v2)
    except Ellipsis as e:
        v3 = "输入数据错误"

    return HttpResponse(v3)