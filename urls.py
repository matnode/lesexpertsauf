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
)
