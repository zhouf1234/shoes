from . import views
# from django.conf.urls import include,url
from django.urls import path,include
from rest_framework import routers

#定义路由
route = routers.DefaultRouter()

#注册新的路由地址(路由到某个序列化的类)
u = route.register(r'user',views.UserViewSet)
s = route.register(r'shoes',views.ShoesViewSet)
#注册上一级的路由地址并添加
urlpatterns = [
    path('api/',include(route.urls)),
]

