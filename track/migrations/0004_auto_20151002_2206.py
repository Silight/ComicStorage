# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0003_book_volume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='bar_code',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.IntegerField(default=1),
        ),
    ]
