from django.db import models

# Create your models here.

class Shoes(models.Model):
    color = models.CharField('颜色', max_length=11)
    size = models.IntegerField('大小')


class User(models.Model):
    name = models.CharField('用户姓名', max_length=256)
    phone = models.CharField('用户电话', max_length=256)
    user_shoes = models.ForeignKey(to='Shoes',on_delete=models.CASCADE)
