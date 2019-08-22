from django.conf.urls import url

from .views import RegisterPageView


app_name = 'accounts'

urlpatterns = [
    url(r'^login/$', 'django.contrib.auth.views.login',
        {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'next_page': 'home:index'}, name='logout'),
    url(r'^register/$', RegisterPageView.as_view(), name='register')
]
