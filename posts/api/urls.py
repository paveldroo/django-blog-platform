from django.conf.urls import url

from posts.api.views import PostListAPIView

urlpatterns = [
    url(r'^$', PostListAPIView.as_view(), name='list'),
    # url(r'^create/$', post_create),
    # url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
    # url(r'^(?P<slug>[\w-]+)/edit/$', post_update, name='update'),
    # url(r'^(?P<slug>[\w-]+)/delete/$', post_delete),
]
