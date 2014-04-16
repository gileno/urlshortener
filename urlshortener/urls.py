from django.conf.urls import patterns, include, url
from django.contrib import admin

from urlshortener.core.views import HomeView, RedirectLinkView

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^(?P<slug>[\w_-]+)$', RedirectLinkView.as_view(), name='link'),
    url(r'^admin/', include(admin.site.urls)),
)
