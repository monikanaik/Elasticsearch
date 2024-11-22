from django.contrib import admin

from app.models import Book, Category, Article


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "description"]


admin.site.register(Book, BookAdmin)
admin.site.register(Category)
admin.site.register(Article)
