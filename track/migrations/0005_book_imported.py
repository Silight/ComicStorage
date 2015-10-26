# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0004_auto_20151002_2206'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='imported',
            field=models.BooleanField(default=False),
        ),
    ]
