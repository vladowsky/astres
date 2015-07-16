# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ditresa', '0017_auto_20150706_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='natal',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 6, 23, 28, 40, 462013, tzinfo=utc), verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='natal',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 6, 23, 28, 40, 462013, tzinfo=utc), verbose_name='Дата обновления'),
        ),
    ]
