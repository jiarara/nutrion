# coding:utf-8
from django import VERSION
from .widgets import UEditorWidget, AdminUEditorWidget
from .views import get_ueditor_controller
from django.urls import re_path as url

urlpatterns = [
    url(r'^controller/$', get_ueditor_controller),
]
