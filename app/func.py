from django.http import HttpResponse
from django.shortcuts import render
from app import models       #导入blog模块
from django.contrib import auth
def get_usertype(request) :
    res=models.UserInfo.objects.filter(username=request.user.username)
    return res[0].usertype

def get_userid(request) :
    res=models.UserInfo.objects.filter(username=request.user.username)
    return res[0].id
def get_allserver() :
    res=models.UserInfo.objects.filter(usertype='server')
    ans=[]
    for item in res :
        tmp=dict()
        tmp['username']=item.username
        tmp['img']=item.img
        tmp['id']="/app/diancan/"+str(item.id)
        ans.append(tmp)
    return ans
def get_dish(serverid):
    res=models.Dishes.objects.filter(serverid=serverid)
    ans=[]
    for item in res:
        tmp=dict()
        tmp['dishname']=item.dishname
        tmp['price']=item.price
        tmp['img']=item.img
        ans.append(tmp)
    return ans
def get_servername(sid) :
    res=models.UserInfo.objects.filter(id=sid);
    return res[0].username
def addonedish(servername,dishname,price):
    res=models.Ordered.objects.filter(servername=servername,dishname=dishname)
    if len(res)==0: 
        models.Ordered.objects.create(servername=servername,dishname=dishname,num=0,price=price)
    res=models.Ordered.objects.get(servername=servername,dishname=dishname)
    res.num+=1
    res.save()

def deleteonedish(servername,dishname,price):
    res=models.Ordered.objects.filter(servername=servername,dishname=dishname)
    if len(res)==0: 
        return
    res=models.Ordered.objects.get(servername=servername,dishname=dishname)
    if res.num>0 :
        res.num-=1
    if res.num==0 :
        res=models.Ordered.objects.filter(servername=servername,dishname=dishname).delete()
    else :
        res.save()
def get_ordered():
    res=models.Ordered.objects.filter()
    ans=[]
    for item in res:
        tmp=dict()
        tmp['servername']=item.servername
        tmp['dishname']=item.dishname
        tmp['price']=item.price
        tmp['num']=item.num
        ans.append(tmp)
    return ans