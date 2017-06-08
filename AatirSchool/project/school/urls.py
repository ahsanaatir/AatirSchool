from django.conf.urls import url
from . import views

app_name = 'school'

urlpatterns = [
    url(r'^$',  views.login_user, name='login_user'),
    url(r'^index/$', views.index, name='index'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    # url(r'^student/$', views.studentView, name='studentView'),
]
