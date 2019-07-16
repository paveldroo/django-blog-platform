from django.conf.urls import url

from .views import post_create, post_delete, post_detail, post_list, post_update

urlpatterns = [
    url(r'^$', post_list),
    url(r'^create/$', post_create),
    url(r'^(?P<id>\d+)', post_detail, name='detail'),
    url(r'^update/$', post_update),
    url(r'^delete/$', post_delete),
]
