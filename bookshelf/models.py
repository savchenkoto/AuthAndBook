from django.db import models
from django.core.urlresolvers import reverse


class Author(models.Model):

    name = models.CharField(max_length=100)
    about = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('bookshelf:authors')


class Book(models.Model):

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()

    def get_absolute_url(self):
        return reverse('bookshelf:books')

    def __str__(self):
        return self.title

