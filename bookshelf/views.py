from django.http import HttpResponse
from django.shortcuts import render
from .models import Author


def index(request):
    authors = Author.objects.all()
    context = { 'authors':authors }
    return render(request, 'bookshelf/index.html', context)

def detail(request, author_id):
    return HttpResponse('<h2>Details for Author ' + author_id + '</h2>')