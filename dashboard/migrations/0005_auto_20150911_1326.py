# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20150524_0020'),
    ]

    operations = [
        migrations.CreateModel(
            name='SwitchStatus',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('status', models.IntegerField()),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('board', models.ForeignKey(related_name='status', to='dashboard.SmartBoard')),
            ],
        ),
        migrations.AlterField(
            model_name='channel',
            name='units',
            field=models.CharField(max_length=50, default='Power'),
        ),
    ]
