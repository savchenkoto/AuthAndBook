from django.conf.urls import url
from django.views.generic import DetailView
from .models import *
from .views import *

app_name = 'bookshelf'

urlpatterns = [

    url(r'^books/$', Books.as_view(), name='books'),

    url(r'^authors/$', Authors.as_view(), name='authors'),

    url(r'^author/(?P<pk>[0-9]+)/$',
        DetailView.as_view(model=Author, template_name='bookshelf/author_detail.html'),
        name='author'),

    url(r'^book/(?P<pk>[0-9]+)/$',
        DetailView.as_view(model=Book, template_name='bookshelf/book_detail.html'),
        name='book'),

    url(r'author/add/$',
        CreateView.as_view(model=Author, fields=['name', 'about'], template_name='bookshelf/model_form.html'),
        name='author-add'),

    url(r'author/(?P<pk>[0-9]+)/delete/$',
        DeleteView.as_view(model=Author, success_url=reverse_lazy('bookshelf:authors')),
        name='author-delete'),

    url(r'author/(?P<pk>[0-9]+)/update/$',
        UpdateView.as_view(model=Author, fields=['name', 'about'], template_name='bookshelf/model_form.html'),
        name='author-update'),

    url(r'book/add/$',
        CreateView.as_view(model=Book, fields=['author', 'title', 'description'],
                           template_name='bookshelf/model_form.html'),
        name='book-add'),

    url(r'book/(?P<pk>[0-9]+)/delete$',
        DeleteView.as_view(model=Book, success_url=reverse_lazy('bookshelf:books')),
        name='book-delete'),

    url(r'book/(?P<pk>[0-9]+)/update$',
        UpdateView.as_view(model=Book, fields=['author', 'title', 'description'],
                           template_name='bookshelf/model_form.html'),
        name='book-update'),

    url(r'books/search/$', BooksSearch.as_view(), name='books-search')

]
