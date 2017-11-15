from django.conf.urls import url
from django.views.generic import DetailView
from .models import *
from .views import *

app_name = 'bookshelf'

urlpatterns = [
    url(r'^$', Books.as_view(), name='books'),
    url(r'^author/(?P<pk>[0-9]+)/$', AuthorDetail.as_view(), name='author'),
    url(r'^authors/$', Authors.as_view(), name='authors'),
    url(r'^book/(?P<pk>[0-9]+)/$', BookDetail.as_view(), name='book'),
]