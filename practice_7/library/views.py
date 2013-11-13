from django.shortcuts import render
from django.template import RequestContext, loader

from library.models import Book
from library.models import Author
from datetime import date

from django.views.generic import DetailView
from django.views.generic import TemplateView
from django.views.generic import ListView

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render

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


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/login/")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {
        'form': form,
    })
