from django.conf.urls import url
from django.contrib import admin
from . import views
app_name="osat"

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^about/$', views.about, name='about'),
    url(r'^registration/$', views.registration, name='registration'),
    url(r'^a_registration/$', views.a_registration, name='a_registration'),

    url(r'^t_registration/$', views.t_registration, name='t_registration'),
    url(r'^t_registration_homecoming/(?P<email>[0-9]+)$', views.t_registration_homecoming, name='t_registration_homecoming'),

    url(r'^h_registration/$', views.h_registration, name='h_registration'),
    url(r'^e_registration/$', views.e_registration, name='e_registration'),
    url(r'^c_us/$', views.c_us, name='c_us'),
    url(r'^payments/$', views.payments, name='payments'),
    url(r'^donations/$', views.donations, name='donations'),
    url(r'^notifications/$', views.notific, name='notific'),
    url(r'^json_sending/$', views.example, name='example'),


    url(r'^ec_registration/$', views.ec_registration, name='ec_registration'),
    url(r'^er_registration/$', views.er_registration, name='er_registration'),
    url(r'^er_registration/(?P<x>[\w\-]+)$', views.er_registration2, name='er_registration2'),
    url(r'^el_registration/$', views.el_registration, name='el_registration'),
    url(r'^el_registration3/$', views.el_registration3, name='el_registration3'),
    url(r'^el_registrationpassmatch/$', views.el_registrationpassmatch, name='el_registrationpassmatch'),


    url(r'^admin2/$', views.admin2, name='admin2'),
    url(r'^admin2/final_list$', views.final_list, name='final_list'),
    url(r'^admin2/final_list/(?P<pk>[0-9]+)$', views.final_list_attend, name='final_list_attend'),
    url(r'^admin2notification/$', views.admin2notification, name='admin2notification'),

    url(r'^tickets/$', views.tickets, name='tickets'),
    url(r'^chasing_infinity/$',views.chasing_infinity, name='chasing_infinity'),

    url(r'^json/$',views.ind, name='ind')

]
