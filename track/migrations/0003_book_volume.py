# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0002_auto_20151002_2059'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='volume',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
