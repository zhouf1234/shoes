from django.contrib import admin
from .models import User,Shoes

# Register your models here.

class ShoesAdmin(admin.ModelAdmin):
    list_display = ('id','color','size')

class UserAdmin(admin.ModelAdmin):
    list_display = ('id','name','phone','user_shoes_id')

admin.site.register(User,UserAdmin)
admin.site.register(Shoes,ShoesAdmin)