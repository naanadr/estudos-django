from django.conf.urls import url
from .views import home, contact

app_name = 'core'

urlpatterns = [
   url(r'^$', home, name='home'),
   url(r'^contato/$', contact, name='contact'),
]
