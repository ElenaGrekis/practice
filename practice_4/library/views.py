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


def show_book(request, book_id):
    book = Book.objects.get(id=book_id)
    template = loader.get_template('book.html')
    context = RequestContext(request, {
        'book': book,
    })
    return HttpResponse(template.render(context))

def show_author(request, author_id): #FIXED IN Task3
    book = Book.objects.get(id=author_id)
    template = loader.get_template('book.html')
    context = RequestContext(request, {
        'book': book,
    })
    return HttpResponse(template.render(context))
