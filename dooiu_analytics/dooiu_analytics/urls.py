"""
URL configuration for dooiu_analytics project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from dooiu_analytics.settings import BASE_DIR
from django.contrib import admin
from django.urls import path
from show_data import views as data_views
from login import views as login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', data_views.hello),
    path('login/', login_view.login, name='login'),
    path('home/', data_views.home, name='home'),
    path('graph/', data_views.graph, name='graph'),
]
