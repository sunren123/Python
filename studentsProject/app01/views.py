from django.shortcuts import render,HttpResponse

# Create your views here.
from app01 import models

def students(request):

    stu_list = models.Student.objects.all()
    cls_list = models.Classes.objects.all()

    return render(request,"students.html",locals())



def add_student(request):
    response = {'status':True,'message': None}
    try:
        u = request.POST.get('username')
        a = request.POST.get('age')
        g = request.POST.get('gender')
        c = request.POST.get('cls_id')
        models.Student.objects.create(
            username=u,
            age=a,
            gender=g,
            cs_id=c
        )
    except Exception as e:
        response['status'] = False
        response['message'] = '用户输入错误'
    import json
    result = json.dumps(response,ensure_ascii=False)
    return HttpResponse(result)