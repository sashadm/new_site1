"""django_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from hello.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('car/<int:id>', car),
    path('cars/', expensive_cars),
    path('filter/<str:color>', color_cars),
    path('filter/<str:mark>', mark_cars),
    path('filter/<str:model>', model_cars),
    path('filter/<str:color>/<str:mark>', cars_color_mark),
    path('add_car/', add_car)
] +static('media/', document_root=settings.MEDIA_ROOT)
