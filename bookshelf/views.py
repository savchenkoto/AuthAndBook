from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, DeleteView, UpdateView
from django.views import generic
from django.urls import reverse_lazy
from django.db.models import Q

from .models import Author, Book


class Authors(ListView):
    template_name = 'bookshelf/authors.html'
    context_object_name = 'authors'
    model = Author

    def get_queryset(self):
        return self.model.objects.all()


class Books(ListView):
    model = Book
    template_name = 'bookshelf/books.html'

    def get_queryset(self):
        return self.model.objects.all()


class BooksSearch(ListView):
    model = Book
    context_object_name = 'query_list'
    template_name = 'bookshelf/search_results.html'

    def get_queryset(self):
        result = self.model.objects.all()
        query = self.request.GET.get('q')
        if query:
            result = result.filter(
                Q(title__icontains=query) |
                Q(author__name__icontains=query)
            )
        return result

    def get_context_data(self, **kwargs):
        context = super(BooksSearch, self).get_context_data(**kwargs)
        context.update({'query': self.request.GET.get('q'),
                        'size': len(self.get_queryset())})
        return context
