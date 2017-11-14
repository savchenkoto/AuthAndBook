from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models import Author


def index(request):
    authors = Author.objects.all()
    context = { 'authors':authors }
    return render(request, 'bookshelf/index.html', context)


def detail(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    context = { 'author' : author}
    return render(request, 'bookshelf/detail.html', context)