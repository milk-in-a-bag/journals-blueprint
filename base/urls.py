from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('users', views.users, name="users"),
    path('statements', views.statements, name="statements"),
    path('committees', views.committees, name="committees"), 
    path('committees/<int:id>/', views.committee_detail, name="committee_detail")
]
