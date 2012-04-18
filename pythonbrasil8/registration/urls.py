# coding: utf-8
from django.conf.urls.defaults import patterns, url

from .views import RegistrationView, CheckoutView


urlpatterns = patterns('',
    url(r'^$', RegistrationView.as_view(), name='form'),
    url(r'^(?P<slug>\w+)/checkout/$', CheckoutView.as_view(), name='checkout'),
)
