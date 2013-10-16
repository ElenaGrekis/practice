from django.db import models
from datetime import datetime
from django.core.urlresolvers import reverse

class Author(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField(null=True)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)
    def get_absolute_url(self):      
        return reverse('show_author',  args=[str(self.id)] )

class Publisher(models.Model):
    title = models.CharField(max_length=32)
    address = models.TextField()
    city = models.CharField(max_length=64)
    country = models.CharField(max_length=64)
    website = models.URLField()

    def __unicode__(self):
        return u'%s (%s, %s)' % (self.title, self.city, self.country)


class Book(models.Model):
    title = models.CharField(max_length=128)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):      
        return reverse('show_book',  args=[str(self.id)] )
    
