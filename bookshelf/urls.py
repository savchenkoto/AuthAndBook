from django.conf.urls import url
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy
from .views import BooksSearch
from .models import Book, Author

app_name = 'bookshelf'

urlpatterns = [

    url(r'^books/$', ListView.as_view(model=Book, template_name='bookshelf/books.html'), name='books'),

    url(r'^authors/$', ListView.as_view(model=Author, template_name='bookshelf/authors.html'), name='authors'),

    url(r'^book/(?P<pk>[0-9]+)/$',
        DetailView.as_view(model=Book, template_name='bookshelf/book_detail.html'),
        name='book'),

    url(r'^author/(?P<pk>[0-9]+)/$',
        DetailView.as_view(model=Author, template_name='bookshelf/author_detail.html'),
        name='author'),

    url(r'author/new/$',
        CreateView.as_view(model=Author, fields=['name', 'about'], template_name='bookshelf/model_form.html'),
        name='author-add'),

    url(r'author/(?P<pk>[0-9]+)/delete/$',
        DeleteView.as_view(model=Author, success_url=reverse_lazy('bookshelf:authors')),
        name='author-delete'),

    url(r'author/(?P<pk>[0-9]+)/update/$',
        UpdateView.as_view(model=Author, fields=['name', 'about'], template_name='bookshelf/model_form.html'),
        name='author-update'),

    url(r'book/new/$',
        CreateView.as_view(model=Book, fields=['author', 'title', 'description'],
                           template_name='bookshelf/model_form.html'),
        name='book-add'),

    url(r'book/(?P<pk>[0-9]+)/delete/$',
        DeleteView.as_view(model=Book, success_url=reverse_lazy('bookshelf:books')),
        name='book-delete'),

    url(r'book/(?P<pk>[0-9]+)/update/$',
        UpdateView.as_view(model=Book, fields=['author', 'title', 'description'],
                           template_name='bookshelf/model_form.html'),
        name='book-update'),

    url(r'books/search/$', BooksSearch.as_view(), name='books-search')

]
