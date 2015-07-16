# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ditresa', '0020_auto_20150706_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='natal',
            name='birth_latitude',
            field=models.FloatField(default=55.75, blank=True, verbose_name='Широта рождения'),
        ),
        migrations.AlterField(
            model_name='natal',
            name='birth_longitude',
            field=models.FloatField(default=37.62, blank=True, verbose_name='Долгота рождения'),
        ),
        migrations.AlterField(
            model_name='natal',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 6, 23, 58, 17, 135188, tzinfo=utc), verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='natal',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 6, 23, 58, 17, 135188, tzinfo=utc), verbose_name='Дата обновления'),
        ),
    ]
