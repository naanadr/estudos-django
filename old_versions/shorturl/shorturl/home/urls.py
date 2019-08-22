from django.conf.urls import url

from .views import HomePageView


app_name = 'home'

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='index'),
]
