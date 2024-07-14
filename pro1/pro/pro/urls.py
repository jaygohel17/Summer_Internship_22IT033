"""
URL configuration for pro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',views.first,
    #      name='first'),
    path('',include('app1.urls'))
    
] + static(settings.MEDIA_URL,document_root 
           = settings.MEDIA_ROOT)


# pip install django
# django-admin startproject project / python -m startproject projectname
# python manage.py runserver
# python manage.py makemigrations and python manage.py migrate
# python manage.py craetesuperuser
# python manage.py stratapp appname
# to connect the created app and project , go to settings.py and in installed apps section add your app name
# in models.py write code for creating table.
# and to implement the code for table run two commands - python manage.py makemigrations and python manage.py migrate.
