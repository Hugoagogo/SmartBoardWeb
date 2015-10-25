# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20150510_1229'),
    ]

    operations = [
        migrations.AddField(
            model_name='powerreading',
            name='value',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
