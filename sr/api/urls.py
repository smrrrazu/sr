from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^$', views.snippet_list),
    url(r'^(?P<pk>[0-9]+)/$', views.snippet_detail),
    url(r'^categories/$', views.category_list),
]

urlpatterns = format_suffix_patterns(urlpatterns)