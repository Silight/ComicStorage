from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,          {'fields':['title', 'volume']}),
        ('Talent',     {'fields':['writer', 'artist', 'publisher']}),
        ('Genre',       {'fields':['genre', 'subgenre', 'rating', 'maturity']}),
        ('Specs', {'fields':['cover_price', 'isbn', 'bar_code', 'published_date', 'medium']}),
        ('Summary',     {'fields':['summary']}),
    ]
    list_display = ('title', 'volume', 'publisher', 'cover_price', 'quantity', 'published_date', 'rating', 'maturity',)
    list_filter = ['publisher', 'published_date', 'quantity', 'rating',]
    search_fields = ['title', 'publisher', 'writer', 'artist', 'summary',]
    save_on_top = True

admin.site.register(Book, BookAdmin)