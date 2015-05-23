# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_powerreading_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='units',
            field=models.CharField(default=b'Power', max_length=50),
        ),
        migrations.AlterField(
            model_name='channel',
            name='board',
            field=models.ForeignKey(related_name='channels', to='dashboard.SmartBoard'),
        ),
    ]
