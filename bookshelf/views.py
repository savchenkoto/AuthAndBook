from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, DeleteView, UpdateView
from django.views import generic
from django.urls import reverse_lazy
from django.db.models import Q

from .models import Author, Book


class BooksSearch(ListView):
    model = Book
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
        kwargs['query'] = self.request.GET.get('q')
        return super().get_context_data(**kwargs)