# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='artist',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='bar_code',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='cover_price',
            field=models.DecimalField(decimal_places=2, blank=True, max_digits=8),
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[('NF', 'Non-Fiction'), ('FI', 'Fiction'), ('SF', 'Science Fiction'), ('FA', 'Fantasy'), ('AA', 'Action Adventure'), ('HR', 'Horror'), ('MY', 'Mystery'), ('HF', 'Historical Fiction'), ('CH', 'Children'), ('SA', 'Satire'), ('DR', 'Drama'), ('RO', 'Romance'), ('PO', 'Poetry')], max_length=2, blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='maturity',
            field=models.CharField(choices=[('1', 'All Ages'), ('2', 'T - Teen'), ('3', 'T+ - Teens and above'), ('4', 'Parental Advisory'), ('5', 'Max: Explicit Content')], max_length=1, blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='medium',
            field=models.CharField(choices=[('COM', 'Comic'), ('TPB', 'Trade Paperback'), ('ANN', 'Annual'), ('MNG', 'Manga'), ('MAG', 'Magazine'), ('BOK', 'Book')], max_length=3, blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='published_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.CharField(max_length=40, blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='rating',
            field=models.CharField(choices=[('1', '1 - Unreadable'), ('2', '2 - Not Good'), ('3', '3 - Average'), ('4', '4 - Pretty Good'), ('5', '5 - Amazing')], max_length=1, blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='subgenre',
            field=models.CharField(choices=[('NF', 'Non-Fiction'), ('FI', 'Fiction'), ('SF', 'Science Fiction'), ('FA', 'Fantasy'), ('AA', 'Action Adventure'), ('HR', 'Horror'), ('MY', 'Mystery'), ('HF', 'Historical Fiction'), ('CH', 'Children'), ('SA', 'Satire'), ('DR', 'Drama'), ('RO', 'Romance'), ('PO', 'Poetry')], max_length=2, blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='summary',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='writer',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
