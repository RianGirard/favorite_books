from django.urls import path 
from . import views 

urlpatterns = [
    path ('', views.index),
    path ('login', views.login),
    path ('register', views.register),
    path ('success', views.success),
    path ('email_valid/', views.email_valid_null),       # this is here for case of zero text value entry
    path ('email_valid/<str:email>', views.email_valid),
    path ('email_regex/', views.email_regex_null),
    path ('email_regex/<str:email>', views.email_regex),
]