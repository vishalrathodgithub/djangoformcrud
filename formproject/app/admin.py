from django.contrib import admin
from .models import Book


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ["book_name", "author", "page", "price"]


admin.site.register(Book, BookAdmin)
