from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,          {'fields':['title', 'volume']}),
        ('Authors',     {'fields':['writer', 'artist', 'publisher']}),
        ('Genre',       {'fields':['genre', 'subgenre', 'rating', 'maturity'], 'classes':['collapse']}),
        ('Information', {'fields':['cover_price', 'isbn', 'bar_code', 'published_date', 'medium'], 'classes':['collapse']}),
        ('Summary',     {'fields':['summary'], 'classes':['collapse']}),
    ]
    list_display = ('title', 'volume', 'publisher', 'cover_price', 'quantity', 'published_date', 'rating', 'maturity',)
    list_filter = ['publisher', 'published_date', 'quantity', 'rating',]
    search_field = ['title', 'publisher', 'writer', 'artist', 'summary',]

admin.site.register(Book, BookAdmin)