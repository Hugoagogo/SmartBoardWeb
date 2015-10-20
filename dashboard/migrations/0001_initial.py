# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('channel_num', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PowerReading',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('channel', models.ForeignKey(to='dashboard.Channel')),
            ],
        ),
        migrations.CreateModel(
            name='SmartBoard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('num_channels', models.IntegerField(default=4)),
            ],
        ),
        migrations.AddField(
            model_name='channel',
            name='board',
            field=models.ForeignKey(to='dashboard.SmartBoard'),
        ),
    ]
