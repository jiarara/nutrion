"""nutrion URL Configuration

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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
#导入静态文件模块
from django.views.static import serve
#导入配置文件里的文件上传配置
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('ueditor/', include('DjangoUeditor.urls')), #添加DjangoUeditor的URL
    re_path('^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),#增加此行
    # path('accounts/login/', auth_views.LoginView.as_view()),

]   #       +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
