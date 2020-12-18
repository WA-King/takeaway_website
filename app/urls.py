from django.urls import path

from . import views,login,user

urlpatterns = [
    path('', views.index),
    path('register/',login.register),
    path('delete/',login.delete),
    path('test/',user.test),
    path('jiacai/<int:page>',user.test2),
    path('diancan/<int:page>',user.test3),
    path('logout/',login.logout),
    path('login/',login.login),
]
