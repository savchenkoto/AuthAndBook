from django.http import HttpResponse
from .models import Author

def index(request):
    html = ''
    authors = Author.objects.all()
    for author in authors:
        url = '/authors/' + str(author.id) + '/'
        html += '<a href=' + url + '>' + author.name + '</a><br>'
    return HttpResponse(html)


def detail(request, author_id):
    return HttpResponse('<h2>Details for Author ' + author_id + '</h2>')