from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models import Author, Book
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

class AuthorDetail(DetailView):
    model = Author
    template_name = 'bookshelf/author-detail.html'


class BookDetail(DetailView):
    model = Book
    template_name = 'bookshelf/book-detail.html'


class Books(ListView):
    template_name = 'bookshelf/books.html'
    context_object_name = 'books'

    def get_queryset(self):
        return Book.objects.all()


class Authors(ListView):
    template_name = 'bookshelf/authors.html'
    context_object_name = 'authors'

    def get_queryset(self):
        return Author.objects.all()


class AuthorCreate(CreateView):
    model = Author
    fields = ['name', 'about']


class AuthorUpdate(UpdateView):
    model = Author
    fields = ['name', 'about']


class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('bookshelf:authors')


class BookCreate(CreateView):
    model = Book
    fields = ['author', 'title', 'description']


class BookUpdate(UpdateView):
    model = Book
    fields = ['author', 'title', 'description']


class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('bookshelf:books')