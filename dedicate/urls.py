from django.urls import path
from . import views


urlpatterns = [
    path("", views.home_page, name="home"),
    path("extract/", views.extract, name="extract"),
    path("ls/", views.list_directory, name="list_directory"),
    path("enable-execution/", views.enable_execution, name="enable_execution"),
    path("execute/", views.execute, name="execution"),
]