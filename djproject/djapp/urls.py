from django.urls import path
from .models import AppConfig
from . import views

admin_page_sufix = AppConfig.objects.get(identifier='general').admin_page_sufix

urlpatterns = [
    path('', views.index, name='index'),
    
    path('home', views.home, name='home'),
    path('home/', views.home, name='home'),

    path('admin{}'.format(admin_page_sufix), views.admin, name='admin'),
    path('admin{}/'.format(admin_page_sufix), views.admin, name='admin'),
]
