from django.http import HttpResponse
from django.shortcuts import render,redirect
from app import models,func       #导入blog模块
from django.contrib import auth
# 表单
def test(request): 
    if request.user.is_authenticated==False:
        return redirect("/app/login")
    utype=func.get_usertype(request)
    if utype=="server":
        sid=func.get_userid(request)
        return redirect("/app/jiacai/"+str(sid))
    mm=func.get_allserver()
    return render(request,'app/gouwu.html',{
        'username':request.user.username,
        'server':mm,
        'num_server':len(mm),
    })

def test2(request,*args,**kwargs): 
    sid=kwargs['page']
    if request.method=="POST":
        action=request.POST.get("action")
        if action=='add':
            dname=request.POST.get("dishname")
            pr=request.POST.get("price")
            img=request.POST.get("img")
            models.Dishes.objects.create(serverid=sid,dishname=dname,price=int(pr),img=img)
        else :
            dname=request.POST.get("dishname")
            models.Dishes.objects.filter(dishname=dname).delete()
    mm=func.get_dish(sid)
    return render(request,'app/jiacai.html',{
        'username':request.user.username,
        'dish':mm,
    })

def test3(request,*args,**kwargs): 
    url = request.path_info
    url= url.split('/')
    sid=url[-1]
    if request.method=="POST":
        action=request.POST.get("action")
        servername=func.get_servername(sid)
        dname=request.POST.get("dishname")
        pr=request.POST.get("price")
        if action=='add':
            func.addonedish(servername,dname,pr)
        else :
            func.deleteonedish(servername,dname,pr)
    mm=func.get_dish(sid)
    allorder=func.get_ordered()
    sumprice=0
    for item in allorder:
        sumprice+=item['price']*item['num']
    return render(request,'app/diancan.html',{
        'username':request.user.username,
        'dish':mm,
        'order':allorder,
        'sumprice':sumprice,
    })