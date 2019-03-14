from django.shortcuts import render,HttpResponse
from .models import User,Shoes
from django.http import JsonResponse

# Create your views here.


#显示所有的user用户信息,不用接口时
def user(request):
    user = User.objects.all()
    for i in user:
        return JsonResponse({
            'success': 'true',
            'message': 'ok',
            'id':i.id,
            'name': i.name,
            'phone':i.phone,
            'shoes':[
                {
                    'color':i.user_shoes.color,
                    'size':i.user_shoes.size,
                    'id':i.user_shoes.id
                }
            ]

        })


from rest_framework import viewsets
from .serializers import UserInfoSerializer,ShoesSerializer
#
class UserViewSet(viewsets.ModelViewSet):
    # queryset指明该视图集在查询数据时使用的查询集
    # serializer_class指明该视图在进行序列化或反序列化时使用的序列化器
    # 指定结果集并设置排序
    queryset = User.objects.all().order_by('id')
    # 指定序列化的类
    serializer_class = UserInfoSerializer

class ShoesViewSet(viewsets.ModelViewSet):
    queryset = Shoes.objects.all().order_by('id')
    # 指定序列化的类
    serializer_class = ShoesSerializer










