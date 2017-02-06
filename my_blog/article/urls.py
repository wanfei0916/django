from django.conf.urls import url
from article import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^(?P<id>\d+)/$', views.detail, name='detail'),
    url(r'^tag/(?P<tag>\w+)/$', views.search_tag, name='search_tag'),
]