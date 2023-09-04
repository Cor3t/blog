from django.urls import path
from . import views
from django.urls import re_path

app_name = 'accounts'

urlpatterns = [
    re_path(r'^signup/$', views.signup_view, name='signup'),
    re_path(r'^login/$', views.login_view, name='login'),
    re_path(r'^logout/$', views.logout_view, name='logout'),
]