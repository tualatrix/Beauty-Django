from django.conf.urls.defaults import patterns, include, url
from usbeauty.views import home,upload,vote,about,top,rate
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', home),
    url(r'^upload/$', upload),
    url(r'^vote/$', vote),
    url(r'^votea/$', vote),
    url(r'^voteb/$', vote),
    url(r'^about/$', about),
    url(r'^top/$', top),
    url(r'^rate/$', rate),
    #url(r'^votea/$', vote),
    #url(r'^voteb/$', vote),
   
    
    # url(r'^usbeauty/', include('usbeauty.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
