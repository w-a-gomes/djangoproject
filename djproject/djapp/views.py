from django.shortcuts import render
from .models import AppConfig


def index(request):
    """General home page"""
    return render(
        request, 'djapp/index.html',
        {
            'app_name': AppConfig.objects.get(identifier='general').name,
            'title_description': 'Index page',
        }
    )


def home(request):
    """User home page"""
    return render(
        request, 'djapp/home.html',
        {
            'app_name': AppConfig.objects.get(identifier='general').name,
            'title_description': 'Home page',
        }
    )


def admin(request):
    """Administrative authentication page"""
    return render(
        request, 'djapp/admin.html',
        {
            'app_name': AppConfig.objects.get(identifier='general').name,
            'title_description': 'Admin auth page',
        }
    )


# Errors
# https://docs.djangoproject.com/pt-br/4.0/intro/tutorial03/#a-shortcut-get-object-or-404

# Templates
# https://docs.djangoproject.com/pt-br/4.0/intro/tutorial03/#use-the-template-system

# url
# https://docs.djangoproject.com/pt-br/4.0/intro/tutorial03/#removing-hardcoded-urls-in-templates

# Namespace url
# https://docs.djangoproject.com/pt-br/4.0/intro/tutorial03/#namespacing-url-names

# Atalhos
# https://www.w3schools.com/html/html_computercode_elements.asp

# Designe Responsivo
# https://www.w3schools.com/html/html_responsive.asp

# Tags
# https://dev.to/thepylot/how-to-add-tags-to-your-models-in-django-django-packages-series-1-3704

# Login
# https://learndjango.com/tutorials/django-login-and-logout-tutorial
# https://docs.djangoproject.com/pt-br/4.0/topics/auth/

# HTML editor
#