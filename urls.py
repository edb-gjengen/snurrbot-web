from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'main.views.home', name='home'),
    # url(r'^snurrweb/', include('snurrweb.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
