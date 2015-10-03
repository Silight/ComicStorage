# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=120)),
                ('writer', models.CharField(max_length=100)),
                ('artist', models.CharField(max_length=100)),
                ('publisher', models.CharField(max_length=40)),
                ('genre', models.CharField(choices=[('NF', 'Non-Fiction'), ('FI', 'Fiction'), ('SF', 'Science Fiction'), ('FA', 'Fantasy'), ('AA', 'Action Adventure'), ('HR', 'Horror'), ('MY', 'Mystery'), ('HF', 'Historical Fiction'), ('CH', 'Children'), ('SA', 'Satire'), ('DR', 'Drama'), ('RO', 'Romance'), ('PO', 'Poetry')], max_length=2)),
                ('subgenre', models.CharField(choices=[('NF', 'Non-Fiction'), ('FI', 'Fiction'), ('SF', 'Science Fiction'), ('FA', 'Fantasy'), ('AA', 'Action Adventure'), ('HR', 'Horror'), ('MY', 'Mystery'), ('HF', 'Historical Fiction'), ('CH', 'Children'), ('SA', 'Satire'), ('DR', 'Drama'), ('RO', 'Romance'), ('PO', 'Poetry')], max_length=2)),
                ('medium', models.CharField(choices=[('COM', 'Comic'), ('TPB', 'Trade Paperback'), ('ANN', 'Annual'), ('MNG', 'Manga'), ('MAG', 'Magazine'), ('BOK', 'Book')], max_length=3)),
                ('published_date', models.DateTimeField(null=True, blank=True)),
                ('cover_price', models.DecimalField(max_digits=8, decimal_places=2)),
                ('isbn', models.IntegerField()),
                ('bar_code', models.IntegerField()),
                ('quantity', models.IntegerField(default=1)),
                ('summary', models.TextField()),
                ('rating', models.CharField(choices=[('1', '1 - Unreadable'), ('2', '2 - Not Good'), ('3', '3 - Average'), ('4', '4 - Pretty Good'), ('5', '5 - Amazing')], max_length=1)),
                ('maturity', models.CharField(choices=[('1', 'All Ages'), ('2', 'T - Teen'), ('3', 'T+ - Teens and above'), ('4', 'Parental Advisory'), ('5', 'Max: Explicit Content')], max_length=1)),
            ],
        ),
    ]
