# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ditresa', '0026_auto_20150706_1906'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='natal',
            name='jupiter',
        ),
        migrations.RemoveField(
            model_name='natal',
            name='mars',
        ),
        migrations.RemoveField(
            model_name='natal',
            name='mercury',
        ),
        migrations.RemoveField(
            model_name='natal',
            name='moon',
        ),
        migrations.RemoveField(
            model_name='natal',
            name='neptun',
        ),
        migrations.RemoveField(
            model_name='natal',
            name='pluto',
        ),
        migrations.RemoveField(
            model_name='natal',
            name='saturn',
        ),
        migrations.RemoveField(
            model_name='natal',
            name='sun',
        ),
        migrations.RemoveField(
            model_name='natal',
            name='uran',
        ),
        migrations.RemoveField(
            model_name='natal',
            name='venus',
        ),
        migrations.AlterField(
            model_name='natal',
            name='created_date',
            field=models.DateTimeField(verbose_name='Дата создания', default=datetime.datetime(2015, 7, 7, 0, 12, 13, 766630, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='natal',
            name='updated_date',
            field=models.DateTimeField(verbose_name='Дата обновления', default=datetime.datetime(2015, 7, 7, 0, 12, 13, 766630, tzinfo=utc)),
        ),
    ]
