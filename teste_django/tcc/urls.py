# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from grafico.views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    'grafico.views',
    url(r'^$', 'home', name='home'),
    url(r'^contato/$', Criar.as_view(), name='contato'),
    url(r'^cadastrogeral/$', Cadastrogeral.as_view(), name='cadastrogeral'),
    url(r'^grafico/$', Grafico.as_view(), name='grafico'),
    url(r'^grafico2/$', Grafico2.as_view(), name='grafico2'),
    url(r'^admin/', include(admin.site.urls)),
)
