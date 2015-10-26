from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,          {'fields':['title', 'volume', 'imported']}),
        ('Talent',      {'fields':['writer', 'artist', 'publisher']}),
        ('Genre',       {'fields':['genre', 'subgenre', 'rating', 'maturity']}),
        ('Specs',       {'fields':['cover_price', 'isbn', 'bar_code', 'published_date', 'medium', 'pages']}),
        ('Summary',     {'fields':['summary']}),
    ]
    list_display = ('title', 'imported', 'volume', 'publisher', 'cover_price', 'quantity', 'published_date', 'rating', 'pages',)
    list_filter = ['publisher', 'published_date', 'quantity', 'rating', 'imported',]
    search_fields = ['title', 'publisher', 'writer', 'artist', 'summary',]
    save_on_top = True

    
admin.site.register(Book, BookAdmin)