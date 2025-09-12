# app/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from django_countries.fields import CountryField
from django_jalali.db import models as jmodels


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    nationality = CountryField(blank=True)


class Publisher(models.Model):
    name = models.CharField(unique=True, max_length=100)


class Book(models.Model):
    isbn_digits = models.CharField(unique=True, max_length=100)
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL)
    price = models.PositiveBigIntegerField(blank=True, default=None)
    publisher = models.ForeignKey(Publisher, on_delete=models.RESTRICT)
    publish_date = jmodels.jDateField()

    @property
    def isbn(self):
        if self.isbn_digits is None:
            return None
        _isbn = self.isbn_digits
        return f"{_isbn[0:3]}-{_isbn[3:4]}-{_isbn[4:6]}-{_isbn[6:12]}-{_isbn[12]}"

    @isbn.setter
    def isbn(self, value):
        if value is None:
            self.isbn_digits = None
        else:
            self.isbn_digits = str(value).replace('-', '')

class Categorization(models.Model):
    title = models.CharField(max_length=100, unique=True)


class BookCategory(models.Model):
    name = models.CharField(max_length=100)
    categorization = models.ForeignKey(Categorization, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book)


class MyUser(AbstractUser):
    email = models.EmailField(unique=True, blank=True)
    favorite_library = models.ManyToManyField(Book)
