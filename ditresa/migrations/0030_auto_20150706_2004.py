# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ditresa', '0029_auto_20150706_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='natal',
            name='birth_longitude',
            field=models.FloatField(blank=True, verbose_name='Долгота рождения', null=True, default=37.62),
        ),
        migrations.AlterField(
            model_name='natal',
            name='created_date',
            field=models.DateTimeField(verbose_name='Дата создания', default=datetime.datetime(2015, 7, 7, 1, 4, 37, 443262, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='natal',
            name='updated_date',
            field=models.DateTimeField(verbose_name='Дата обновления', default=datetime.datetime(2015, 7, 7, 1, 4, 37, 444262, tzinfo=utc)),
        ),
    ]
