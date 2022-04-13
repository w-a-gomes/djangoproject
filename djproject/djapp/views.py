from django.shortcuts import render
from .models import AppConfig

def index(request):
    return render(
        request, 'djapp/index.html',
        {
            'app_name': AppConfig.objects.get(identifier='general').name,
            'title_description': 'Index page',
        }
    )


def home(request):
    return render(
        request, 'djapp/home.html',
        {
            'app_name': AppConfig.objects.get(identifier='general').name,
            'title_description': 'Home page',
        }
    )


def admin(request):
    return render(
        request, 'djapp/admin.html',
        {
            'app_name': AppConfig.objects.get(identifier='general').name,
            'title_description': 'Admin auth page',
        }
    )