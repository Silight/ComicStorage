from django.db import models
from django.utils import timezone


FORM = (
    ('COM', 'Comic'),
    ('TPB', 'Trade Paperback'),
    ('ANN', 'Annual'),
    ('MNG', 'Manga'),
    ('MAG', 'Magazine'),
    ('BOK', 'Book'),
)

RATING = (
    ('1', '1 - Unreadable'),
    ('2', '2 - Not Good'),
    ('3', '3 - Average'),
    ('4', '4 - Pretty Good'),
    ('5', '5 - Amazing'),
)

MATURITY = (
    ('1', 'All Ages'), 
    ('2', 'T - Teen'),
    ('3', 'T+ - Teens and above'),
    ('4', 'Parental Advisory'), 
    ('5', 'Max: Explicit Content'),
)

GENRE = (
    ('NF', 'Non-Fiction'),
    ('FI', 'Fiction'),
    ('SF', 'Science Fiction'), 
    ('FA', 'Fantasy'), 
    ('AA', 'Action Adventure'), 
    ('HR', 'Horror'), 
    ('MY', 'Mystery'),
    ('HF', 'Historical Fiction'),
    ('CH', 'Children'),
    ('SA', 'Satire'), 
    ('DR', 'Drama'), 
    ('RO', 'Romance'), 
    ('PO', 'Poetry'), 
    
)


class Book(models.Model):   
    title = models.CharField(max_length=120)
    volume = models.IntegerField(blank=True, default=0)
    writer = models.CharField(max_length=100, blank=True)
    artist = models.CharField(max_length=100, blank=True)
    publisher = models.CharField(max_length=40, blank=True)
    genre = models.CharField(max_length=2, choices=GENRE, blank=True)
    subgenre = models.CharField(max_length=2, choices=GENRE, blank=True)
    medium = models.CharField(max_length=3, choices=FORM, blank=True)
    published_date = models.DateField(blank=True, null=True)
    cover_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True)
    isbn = models.IntegerField(blank=True)
    bar_code = models.IntegerField(blank=True)
    quantity = models.IntegerField(default=1)
    summary = models.TextField(blank=True)
    rating = models.CharField(max_length=1, choices=RATING, blank=True)
    maturity = models.CharField(max_length=1, choices=MATURITY, blank=True)
    
    def __str__(self):
        return self.title
