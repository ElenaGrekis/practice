from django.http import HttpResponse
from django.template import RequestContext, loader

from library.models import Book
from library.models import Author


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

def show_author(request, author_id):
    author = Author.objects.get(id=author_id)
    template = loader.get_template('author.html')
    context = RequestContext(request, {
        'author': author,
    })
    return HttpResponse(template.render(context))


def list_authors(request):
    authors = Author.objects.all()
    template = loader.get_template('list_authors.html')
    context = RequestContext(request, {
        'authors': authors,
    })
    return HttpResponse(template.render(context))

