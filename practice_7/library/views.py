from django.shortcuts import render
from django.template import RequestContext, loader

from library.models import Book
from library.models import Author
from datetime import date

from django.views.generic import DetailView
from django.views.generic import TemplateView
from django.views.generic import ListView

class BookListView(ListView):
    template_name = "book_list.html"
    model = Book


class AuthorListView(ListView):
    template_name = "author_list.html"
    model = Author


class BookDetailView(DetailView):
    template_name = "book_detail.html"
    queryset = Book.objects.all()


class AuthorDetailView(DetailView):
    template_name = "author_detail.html"
    queryset = Author.objects.all()
