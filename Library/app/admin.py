from django.contrib import admin
from .models import Author, Publisher, Book, Categorization, BookCategory, MyUser

# Register models
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(Categorization)
admin.site.register(BookCategory)
admin.site.register(MyUser)
