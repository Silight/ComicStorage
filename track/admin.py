from django.contrib import admin
from import_export.admin import ImportExportMixin, ImportExportModelAdmin
from import_export import resources

from .models import Book



class BookResource(resources.ModelResource):

    class Meta:
        model = Book
        fields = ('id', 'title', 'published_date', 'cover_price', 'quantity', 'isbn', 'bar_code', 'publisher',)
        export_order = ('quantity', 'published_date', 'title', 'cover_price', 'isbn', 'bar_code', 'publisher',)
        import_id_fields = ('title')
        
class BookAdmin(ImportExportMixin, admin.ModelAdmin):
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
    resource_class = BookResource

    
admin.site.register(Book, BookAdmin)