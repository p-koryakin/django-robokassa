#coding: utf-8
try:
    from django.conf.urls.defaults import url
except ImportError:
    from django.conf.urls import url

from robokassa.views import fail, receive_result, success
    

urlpatterns = [
    url(r'^result/$', receive_result, name='robokassa_result'),
    url(r'^success/$', success, name='robokassa_success'),
    url(r'^fail/$', fail, name='robokassa_fail'),
]
