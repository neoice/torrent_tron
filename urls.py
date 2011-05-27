from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    # Example:
    # (r'^torrent_tron/', include('torrent_tron.foo.urls')),
)
