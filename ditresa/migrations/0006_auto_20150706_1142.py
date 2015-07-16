# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ditresa', '0005_auto_20150706_0944'),
    ]

    operations = [
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('planet', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Planet',
                'verbose_name_plural': 'Planets',
            },
        ),
        migrations.CreateModel(
            name='Zodiak',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('sign', models.CharField(max_length=20)),
                ('degree', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Zodiac',
                'verbose_name_plural': 'Zodiacs',
            },
        ),
        migrations.AlterField(
            model_name='natal',
            name='birth_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 6, 16, 42, 17, 569908, tzinfo=utc), verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='natal',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 6, 16, 42, 17, 570908, tzinfo=utc), verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='natal',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 6, 16, 42, 17, 570908, tzinfo=utc), verbose_name='Дата обновления'),
        ),
    ]
