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
    (r'^$',"loguin.views.bemVindo"),
    (r'^login/',"django.contrib.auth.views.login",{"template_name":"login.html"}),
    (r'^logout/',"django.contrib.auth.views.logout_then_login",{"login_url":"/login/"}),
    (r'^media/(.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
    (r'^registrar/$','loguin.views.registrar'),
    (r'^bemVindo/$','loguin.views.bemVindo'),
    (r'^grupo/$','grupo.views.grupo'),
)
"""
if settings.DEBUG:
    urlpatterns +=patterns('',
       (r'^media/(?P<path>.*)$','django.views.static.serve',
        {'document_root':settings.MEDIA_ROOT}),
    )"""
