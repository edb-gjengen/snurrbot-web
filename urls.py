from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns # for dev
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'snurrweb.main.views.home', name='home'),
    url(r'^log/$', 'snurrweb.main.views.log', name='log'),
    # url(r'^snurrweb/', include('snurrweb.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

#urlpatterns += staticfiles_urlpatterns()
