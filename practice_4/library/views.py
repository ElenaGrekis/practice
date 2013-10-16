from django.http import HttpResponse
from django.template import RequestContext, loader

from library.models import Book


def index(request):
    books = Book.objects.all()
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'books': books,
    })
    return HttpResponse(template.render(context))


def show(request, book): #FIXED in task2
    books = Book.objects.all()
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'books': books,
    })
    return HttpResponse(template.render(context))
