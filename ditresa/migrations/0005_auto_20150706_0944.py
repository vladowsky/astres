# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ditresa', '0004_auto_20150608_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='natal',
            name='birth_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 6, 14, 44, 34, 312961, tzinfo=utc), verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='natal',
            name='birth_place',
            field=models.CharField(default='Moscow', max_length=255, verbose_name='Место рождения'),
        ),
        migrations.AlterField(
            model_name='natal',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 6, 14, 44, 34, 313960, tzinfo=utc), verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='natal',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 6, 14, 44, 34, 313960, tzinfo=utc), verbose_name='Дата обновления'),
        ),
    ]
