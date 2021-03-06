"""khu_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from . import views as main


from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^services/(?P<slug>[-\w]+)/$', main.ServicesDetail.as_view(), name='service-detail'),
    url(r'^services/$', main.Services.as_view(), name='services'),
    url(r'^services-list/$', main.ServicesList.as_view(), name='services-list'),


]

