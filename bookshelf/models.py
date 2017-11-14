from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos', null=True, blank=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    cover = models.ImageField(upload_to='covers', null=True, blank=True)

    def __str__(self):
        return self.title

