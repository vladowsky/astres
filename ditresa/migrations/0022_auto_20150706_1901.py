# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ditresa', '0021_auto_20150706_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='natal',
            name='birth_latitude',
            field=models.FloatField(null=True, verbose_name='Широта рождения', default=55.75, blank=True),
        ),
        migrations.AlterField(
            model_name='natal',
            name='created_date',
            field=models.DateTimeField(verbose_name='Дата создания', default=datetime.datetime(2015, 7, 7, 0, 1, 53, 952980, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='natal',
            name='updated_date',
            field=models.DateTimeField(verbose_name='Дата обновления', default=datetime.datetime(2015, 7, 7, 0, 1, 53, 953979, tzinfo=utc)),
        ),
    ]
