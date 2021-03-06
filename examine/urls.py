"""euler URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.contrib import admin

from . import views

# TODO: DO YOU SEE THAT THE URL HAS NO $...??? ITS BECAUSE WE WANNA HAVE A SINGLE VIEW FOR ALL THE THINGS LIKE KEYLOGGER

urlpatterns = [
    url(r'^dashboard/$', views.dashboard),

    url(r'^keylogger/$', views.keylogger),

    url(r'^keylogger/(?P<keylog_num>[0-9]*)', views.keylog_record),
]
