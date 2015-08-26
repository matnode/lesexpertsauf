# -*- encoding: utf-8 -*-

from django.conf.urls.defaults import *
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('experts.views',
    (r'^login/$', 'index'),
    (r'^deconnexion/$', 'deconnexion'),
    (r'^inscription/$', 'inscription'),
    (r'^acceuil/$', 'acceuil'),
    (r'^profil/(?P<user_id>\d+)/$', 'profil'),
    (r'^profilcords/(?P<user_id>\d+)/$', 'profilcords'),
    (r'^profilcompetence/(?P<user_id>\d+)/$', 'profilcompetence'),
    (r'^modprofilcompetence/(?P<user_id>\d+)/$', 'modprofilcompetence'),
    (r'^delprofilcompetence/(?P<user_id>\d+)/$', 'delprofilcompetence'),
    (r'^profilmission/(?P<user_id>\d+)/$', 'profilmission'),
    (r'^modprofilmission/(?P<user_id>\d+)/$', 'modprofilmission'),
    (r'^delprofilmission/(?P<user_id>\d+)/$', 'delprofilmission'),
    (r'^profilformation/(?P<user_id>\d+)/$', 'profilformation'),
    (r'^modprofilformation/(?P<user_id>\d+)/$', 'modprofilformation'),
    (r'^delprofilformation/(?P<user_id>\d+)/$', 'delprofilformation'),
    (r'^profilangue/(?P<user_id>\d+)/$', 'profilangue'),
    (r'^modprofilangue/(?P<user_id>\d+)/$', 'modprofilangue'),
    (r'^delprofilangue/(?P<user_id>\d+)/$', 'delprofilangue'),
    (r'^profiloisir/(?P<user_id>\d+)/$', 'profiloisir'),
    (r'^modprofiloisir/(?P<user_id>\d+)/$', 'modprofiloisir'),
    (r'^delprofiloisir/(?P<user_id>\d+)/$', 'delprofiloisir'),
    
)
