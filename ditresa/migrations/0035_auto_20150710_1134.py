# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ditresa', '0034_auto_20150710_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='natal',
            name='birth_date_time',
            field=models.CharField(verbose_name='Birth date', max_length=50),
        ),
        migrations.AlterField(
            model_name='natal',
            name='created_date',
            field=models.DateTimeField(verbose_name='Date of creation', default=datetime.datetime(2015, 7, 10, 16, 34, 0, 536206, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='natal',
            name='updated_date',
            field=models.DateTimeField(verbose_name='Date of update', default=datetime.datetime(2015, 7, 10, 16, 34, 0, 536206, tzinfo=utc)),
        ),
    ]
