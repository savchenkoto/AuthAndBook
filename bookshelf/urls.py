from django.conf.urls import url
from django.views.generic import DetailView
from .models import *
from .views import *

app_name = 'bookshelf'

urlpatterns = [
    url(r'^author/(?P<pk>[0-9]+)/$', AuthorDetail.as_view(), name='author'),
    url(r'^book/(?P<pk>[0-9]+)/$', BookDetail.as_view(), name='book'),
    url(r'^books/$', Books.as_view(), name='books'),
    url(r'^authors/$', Authors.as_view(), name='authors'),

    url(r'author/add/$', AuthorCreate.as_view(), name='author-add'),
    url(r'author/(?P<pk>[0-9]+)/delete/$', AuthorDelete.as_view(), name='author-delete'),
    url(r'author/(?P<pk>[0-9]+)/update/$', AuthorUpdate.as_view(), name='author-update'),

    url(r'book/add/$', BookCreate.as_view(), name='book-add'),
    url(r'book/(?P<pk>[0-9]+)/delete$', BookDelete.as_view(), name='book-delete'),
    url(r'book/(?P<pk>[0-9]+)/update$', BookUpdate.as_view(), name='book-update')
]
