from django.contrib import admin
from django.contrib.contenttypes import generic
from library.models import Book, BooksImage, Publisher
from django.contrib.contenttypes.models import ContentType


class ImageInline(generic.GenericTabularInline):
    model = BooksImage
    extra = 0


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'publisher', 'publication_date', 'books']
    fields = ['title', 'authors', 'publisher']

    def books(self, obj):
        return BooksImage.objects.filter(book_id=obj.id).count()

    inlines = [
        ImageInline,
    ]


admin.site.register(Book, BookAdmin)
