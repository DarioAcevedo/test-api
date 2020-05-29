from django.urls import path
from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework.documentation import include_docs_urls
from .apiviews import parseFecha

urlpatterns=[
    path('v4/login-drf/', views.obtain_auth_token, name="login_drf"),
    path('v4/fechas/', parseFecha.as_view(), name="fecha"),
]
