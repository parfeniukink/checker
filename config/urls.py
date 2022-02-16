from core.views import Analytics
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", Analytics.as_view()),
]
