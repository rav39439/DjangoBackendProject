from django.contrib import admin

# Register your models here.

from bookcollection.models import Book, Review

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'genre', 'published_year')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'username', 'comment')

# admin.site.register(Book)
# admin.site.register(Review)
