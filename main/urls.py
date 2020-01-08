from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.views.generic.base import TemplateView
from rest_framework.routers import DefaultRouter
from main.views import render_react
from main.api_views import *

router = DefaultRouter()
router.register('schools', SchoolViewSet)

urlpatterns = [
    url(r'^app/*', render_react, name='main'),
]