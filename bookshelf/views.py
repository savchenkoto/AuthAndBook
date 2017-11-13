from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>Welcome!</h1>')


def detail(request, book_id):
    return HttpResponse('<h2>Details for Book ' + book_id + '</h2>')