from django.http import HttpResponse
from django.shortcuts import render,redirect
from app import models,func       #导入blog模块
from django.contrib import auth
# 表单
def login(request):
    if request.user.is_authenticated:
        return redirect("/app/test")
    s=""
    if request.method=="POST" :
        uname=request.POST.get("username")
        pd=request.POST.get("password")
        user = auth.authenticate(username=uname,password=pd)
        if user:
            auth.login(request,user)
            return redirect("/app/test")
        else :
            s="fail"
    return render(request,'app/test.html',{
        'message':s,
    })
def logout(request) :
    auth.logout(request)
    return HttpResponse("<a href=\"/app/\">bye bye</a>")
def register(request):
    if request.method=="POST" :
        uname=request.POST.get("username")
        pd=request.POST.get("password")
        utype=request.POST.get("usertype")
        img=request.POST.get("img")
        models.UserInfo.objects.create(username=uname,password=pd,usertype=utype,img=img)
        auth.models.User.objects.create_user(username=uname,password=pd)
        return HttpResponse(uname+' '+pd)
    return render(request,'app/register.html')
def delete(request) :
    name=request.user.username
    auth.logout(request)
    models.UserInfo.objects.filter(username=name).delete()
    auth.models.User.objects.filter(username=name).delete()
    return HttpResponse("bye bye")
# 接收请求数据
def login_nice(request):  
    if request.method=="POST" :
        username=request.POST.get("username")
        password=request.POST.get("password")
        return HttpResponse(username+' '+password)