# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ditresa', '0033_auto_20150707_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='natal',
            name='birth_date_time',
            field=models.CharField(max_length=50, verbose_name='Birthdate'),
        ),
        migrations.AlterField(
            model_name='natal',
            name='birth_latitude',
            field=models.FloatField(default=55.75, blank=True, null=True, verbose_name='Birth latitude'),
        ),
        migrations.AlterField(
            model_name='natal',
            name='birth_longitude',
            field=models.FloatField(default=37.62, blank=True, null=True, verbose_name='Birth longitude'),
        ),
        migrations.AlterField(
            model_name='natal',
            name='birth_place',
            field=models.CharField(default='Moscow', max_length=255, verbose_name='Birth place'),
        ),
        migrations.AlterField(
            model_name='natal',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 10, 16, 30, 43, 918257, tzinfo=utc), verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='natal',
            name='person',
            field=models.CharField(max_length=50, verbose_name='Person name'),
        ),
        migrations.AlterField(
            model_name='natal',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 10, 16, 30, 43, 918257, tzinfo=utc), verbose_name='Дата обновления'),
        ),
    ]
