from django.http import Http404
from django.shortcuts import render
from .models import Author


def index(request):
    authors = Author.objects.all()
    context = { 'authors':authors }
    return render(request, 'bookshelf/index.html', context)


def detail(request, author_id):
    try:
        author = Author.objects.get(id=author_id)
    except Author.DoesNotExist:
        raise Http404("Sorry, authot doesn't exist")
    context = { 'author' : author}
    return render(request, 'bookshelf/detail.html', context)