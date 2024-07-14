from django.urls import path,include
from .views import first,second,table,cattable,form,catform,update,index


urlpatterns = [
    path('',first,name='first'),
    path('second/',second,name='second'),
    path('table/',table,name='table'),
    path('cattable/',cattable,name='cattable'),
    path('form/',form,name='form'),
    path('catform/',catform,name='catform'),
    path('update/',update,name='update'),
    path('index/',index,name='index'),
    

 
] 