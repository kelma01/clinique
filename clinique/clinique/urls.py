"""
URL configuration for clinique project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from django.views.generic import TemplateView
from .views import send_message

urlpatterns = [
    # path('admin/', admin.site.urls), 
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('botoks/', TemplateView.as_view(template_name='pages/botoks.html'), name='botoks'),
    path('dolgu/', TemplateView.as_view(template_name='pages/dolgu.html'), name='dolgu'),
    path('mezoterapi/', TemplateView.as_view(template_name='pages/mezoterapi.html'), name='mezoterapi'),
    path('iletisim/', TemplateView.as_view(template_name='pages/iletisim.html'), name='iletisim'),
    path('contact/submit/', send_message, name='send-message'),
]
