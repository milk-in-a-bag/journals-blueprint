from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('login', views.login_view, name='login'),
    path('signup', views.signup_view, name='signup'),
    path('logout', views.logout_view, name='logout'),
    path('complete-profile', views.complete_profile, name='complete-profile')
]
