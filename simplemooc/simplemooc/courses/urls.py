from django.conf.urls import url

from .views import index, details

app_name = 'courses'

urlpatterns = [
    url(r'^$', index, name='index'),
    # url(r'^(?P<pk>\d+)/$', 'details', name='details'),
    url(r'^(?P<slug>[\w_-]+)/$', details, name='details'),
]
