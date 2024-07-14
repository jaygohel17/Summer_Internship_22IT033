from django.contrib import admin
from .models import Blog,Author,userregister,image,category

# Register your models here.

admin.site.register(Blog)

class author_(admin.ModelAdmin):
    list_display = ['name','email']
    list_filter = ['name','email']
    search_fields = ['name','email']
admin.site.register(Author,author_)

class user_(admin.ModelAdmin):
    list_display = ['name','email','add','password']

admin.site.register(userregister,user_)

admin.site.register(image)

class cat_(admin.ModelAdmin):
    list_display = ['name','image']

admin.site.register(category,cat_)