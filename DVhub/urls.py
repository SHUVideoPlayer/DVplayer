"""DVhub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
import User.views
import main.views
from video import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Register/',User.views.Register),
    path('',main.views.test,name='index'),
    path('login/',User.views.signin,name='login'),
    path('logout/',User.views.logout,name='logout'),
    path('user',User.views.UserPage,name='user'),
    path('vupload/',views.vupload,name='upload'),
    path('vmodify/<int:dvcode>', views.vmodify, name='modify'),
    path('vplay/<int:dvcode>', views.vplay, name='vplay'),
    path('profile/',User.views.profile,name='profile'),
    path('password/',User.views.password,name='password'),
    path('imgcenter/',User.views.imgcenter,name='imgcenter'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


