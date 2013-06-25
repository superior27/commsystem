from django.conf.urls.defaults import *

from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^commsystem/', include('commsystem.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^$',"loguin.views.bem_vindo"),
    (r'^login/',"django.contrib.auth.views.login",{"template_name":"login.html"}),
    (r'^logout/',"django.contrib.auth.views.logout_then_login",{"login_url":"/login/"}),
    (r'^media/(.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
    (r'^registrar/$','loguin.views.registrar'),
    (r'^bem_vindo/$','loguin.views.bem_vindo'),
    (r'^criar_grupo/$','loguin.views.criar_grupo'),
    (r'^cadastrar_usuario_grupo/$','loguin.views.cadastrar_usuario_grupo'),
    (r'^atividade/$','loguin.views.atividade'),
    (r'^lista_atividade/$','loguin.views.lista_atividade'),
    (r'^leia_mais/$','loguin.views.leia_mais'),
    (r'^comments/',include('django.contrib.comments.urls')),
    (r'^cadastrar_permissao_grupo/$','loguin.views.cadastrar_permissao_grupo'),
    (r'^quant_atividade/$','loguin.views.quant_atividade'),
)
"""
if settings.DEBUG:
    urlpatterns +=patterns('',
       (r'^media/(?P<path>.*)$','django.views.static.serve',
        {'document_root':settings.MEDIA_ROOT}),
    )"""
