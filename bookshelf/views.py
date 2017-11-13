from django.http import HttpResponse
from django.template import loader
from .models import Author


def index(request):
    authors = Author.objects.all()
    template = loader.get_template('bookshelf/index.html')
    context = {
        'authors':authors,
    }
    return HttpResponse(template.render(context=context, request=request))


def detail(request, author_id):
    return HttpResponse('<h2>Details for Author ' + author_id + '</h2>')