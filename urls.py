# -*- encoding: utf-8 -*-

from django.conf.urls.defaults import *
from django.conf.urls.static import static
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('experts.views',
    (r'^login/$', 'index'),
    (r'^deconnexion/$', 'deconnexion'),
    (r'^inscription/$', 'inscription'),
    (r'^$', 'acceuil'),
    (r'^routeur/$', 'routeur'),
    #profil expert
    (r'^profil/(?P<user_id>\d+)/$', 'profil'),
    (r'^profil/(?P<human_id>\d+)/photo/$', 'photoprofil'),
    (r'^profilinfo/(?P<user_id>\d+)/$', 'profilinfo'),
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
    (r'^reglages/$', 'reglages'),
    (r'^motdepasse/$', 'motdepasse'),
    #listing des experts 
    (r'^listexperts/$','lesexperts'),   
    (r'^detailexpert/(?P<user_id>\d+)/$','detailexpert'),
    #recherche des donnees experts, entreprise ou offre
    (r'^recherchedesdonnees/$','recherchedesdonnees'),
    #entreprise
    (r'^listentreprise/$', 'listentreprise'),
    (r'^detailentreprise/(?P<user_id>\d+)/$','detailentreprise'),
    (r'^profilentreprise/$', 'profilentreprise'),
    (r'^photoprofilentreprise/$', 'photoprofilentreprise'),
    (r'^profilentrepriseinfo/$', 'profilentrepriseinfo'),
    (r'^profilentreprisecoord/$', 'profilentreprisecoord'),
    (r'^profilentreprisedescription/$', 'profilentreprisedescription'),
    (r'^profilentrepriseactivite/$', 'profilentrepriseactivite'),
    #offre
    (r'^mesoffres/$', 'mesoffres'),
    (r'^lesoffres/$', 'lesoffres'),
    (r'^detailoffre/(?P<offre_id>\d+)/$', 'detailoffre'),
    (r'^detailmonoffre/(?P<offre_id>\d+)/$', 'detailmonoffre'),
    (r'^misajouroffre/(?P<offre_id>\d+)/$', 'misajouroffre'),
    (r'^deloffres/$', 'deloffres'),
    #admin
 )

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += patterns('',
    (r'^admin/', include(admin.site.urls)),
)
