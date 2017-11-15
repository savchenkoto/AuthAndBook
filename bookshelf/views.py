from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models import Author, Book
from django.views import generic


class AuthorDetail(generic.DetailView):
    model = Author
    template_name = 'bookshelf/author-detail.html'


class BookDetail(generic.DetailView):
    model = Book
    template_name = 'bookshelf/book-detail.html'


class Authors(generic.ListView):
    template_name = 'bookshelf/authors.html'
    context_object_name = 'authors'

    def get_queryset(self):
        return Author.objects.all()


class Books(generic.ListView):
    template_name = 'bookshelf/books.html'
    context_object_name = 'books'

    def get_queryset(self):
        return Book.objects.all()


