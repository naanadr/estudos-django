from django.conf.urls import include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = [
    url(r'^$', include('shorturl.home.urls', namespace='home')),
    url(r'^accounts/',
        include('shorturl.accounts.urls', namespace='accounts')),
    url(r'^admin/', include(admin.site.urls)),
]
