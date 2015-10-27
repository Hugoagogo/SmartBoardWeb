# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='smartboard',
            name='num_channels',
        ),
        migrations.AddField(
            model_name='channel',
            name='name',
            field=models.CharField(default='DummyName', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='powerreading',
            name='channel',
            field=models.ForeignKey(related_name='points', to='dashboard.Channel'),
        ),
    ]
