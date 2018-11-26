from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.shortcuts import render_to_response



def set_cookie(request):

    response = HttpResponse("设置cookie")
    response.set_cookie("num",1,max_age=14*24*3600)

    return response

def get_cookie(request):
    num = request.COOKIES["num"]
    return HttpResponse(num)


