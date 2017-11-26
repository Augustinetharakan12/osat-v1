from django.conf.urls import url
from django.contrib import admin
from . import views
app_name="osat"

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^about/$', views.about, name='about'),
    url(r'^a_registration/$', views.a_registration, name='a_registration'),
    url(r'^h_registration/$', views.h_registration, name='h_registration'),
    url(r'^e_registration/$', views.e_registration, name='e_registration'),
    url(r'^c_us/$', views.c_us, name='c_us'),
    url(r'^notifications/$', views.notific, name='notific'),
    url(r'^example/$', views.example, name='example'),


    url(r'^ec_registration/$', views.ec_registration, name='ec_registration'),
    url(r'^er_registration/$', views.er_registration, name='er_registration'),
    url(r'^er_registration/(?P<x>[\w\-]+)$', views.er_registration2, name='er_registration2'),
    url(r'^el_registration/$', views.el_registration, name='el_registration'),
    url(r'^el_registration3/$', views.el_registration3, name='el_registration3'),
    url(r'^el_registrationpassmatch/$', views.el_registrationpassmatch, name='el_registrationpassmatch'),


    url(r'^admin2/$', views.admin2, name='admin2'),
    url(r'^admin2notification/$', views.admin2notification, name='admin2notification'),

]
