
from django.db import models



class Book(models.Model):

    name = models.CharField(max_length=20)
    price = models.IntegerField()
    pub_date = models.DateTimeField()
    publish = models.ForeignKey("Publish")


    def __str__(self):
        return self.name

class Book_Author(models.Model):
    book = models.ForeignKey("Book")
    author = models.ForeignKey("Author")
    def __str__(self):
        return self.name

class Publish(models.Model):

    name = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(max_length=20,default=20)

    def __str__(self):
        return self.name