from rest_framework import serializers
from .models import User,Shoes


class ShoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shoes
        fields = ('id','color','size',)

class UserInfoSerializer(serializers.ModelSerializer):
    """数据序列化器"""
    # shoes_color = serializers.CharField(source='user_shoes.color')
    # shoes_size = serializers.CharField(source='user_shoes.size')
    class Meta:
        model = User
        # fields = ('id', 'name', 'phone', 'user_shoes_id','shoes_color','shoes_size')  # 需要序列化的属性
        fields = '__all__'  # 所有属性



