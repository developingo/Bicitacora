# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url, include

urlpatterns = patterns('xbapp.views',
    url(r'^$', 'inicio'),
    url(r'^login$', 'login'),
    url(r'^logout$', 'logout'),
    url(r'^perfil$', 'perfil'),
    url(r'^captura$', 'captura'),
    url(r'^proyecto$', 'proyecto'),
    url(r'^estadisticas$', 'estadisticas'),
    url(r'^contacto$', 'contacto'),
)

urlpatterns += patterns('xbapp.api',
    url(r'^api$', 'inicio'),
    url(r'^api/registro$', 'registro'),
    url(r'^api/login$', 'login'),
    url(r'^api/token$', 'obtener_token'),
    url(r'^api/w/ruta$', 'registra_ruta'),
    url(r'^api/w/lugar$', 'registra_lugar'),
    url(r'^api/r/rutas$', 'rutas'),
)
