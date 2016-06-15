from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^$', views.SnippetList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
    url(r'^categories/$', views.CategoryList.as_view()),
    url(r'^categories/(?P<pk>[0-9]+)/$', views.CategoryDetail.as_view()),
    url(r'^products/$', views.ProductList.as_view()),
    url(r'^products/(?P<pk>[0-9]+)/$', views.ProductDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)