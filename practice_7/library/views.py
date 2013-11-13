from django.shortcuts import render
from django.template import RequestContext, loader

from library.models import Book
from library.models import Author
from datetime import date


def index(request):
    books = Book.objects.all()
    context = {
        'books': books,
    }
    return render(request, 'index.html', context)


def show_book(request, book_id):
    book = Book.objects.get(id=book_id)
    context = {
        'book': book,
    }
    return render(request, 'book.html', context)


def show_author(request, author_id):
    author = Author.objects.get(id=author_id)
    age = date.today().year - author.birthyear if author.birthyear else 0
    context = {
        'author': author,
        'age': age,
    }
    return render(request, 'author.html', context)


def list_authors(request):
    authors = Author.objects.all()
    context = {
        'authors': authors,
    }
    return render(request, 'list_authors.html', context)
