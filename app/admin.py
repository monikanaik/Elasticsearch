from django.contrib import admin

from app.models import Book


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "description"]


admin.site.register(Book, BookAdmin)
