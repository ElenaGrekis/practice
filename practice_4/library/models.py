from django.db import models
from datetime import datetime

class Author(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField(null=True)

    def __unicode__(self):
        return self.first_name + self.last_name

class Publisher(models.Model):
    title = models.CharField(max_length=32)
    address = models.TextField()
    city = models.CharField(max_length=64)
    country = models.CharField(max_length=64)
    website = models.URLField()

    def __unicode__(self):
        return self.title + "(" + self.website + ")"


class Book(models.Model):
    title = models.CharField(max_length=128)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.title
    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('show',  args=[str(self.id)] )
    
