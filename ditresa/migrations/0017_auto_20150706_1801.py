# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ditresa', '0016_auto_20150706_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='natal',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 6, 23, 1, 12, 672331, tzinfo=utc), verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='natal',
            name='jupiter',
            field=models.CharField(max_length=20, default='', verbose_name='Jupiter'),
        ),
        migrations.AlterField(
            model_name='natal',
            name='mars',
            field=models.CharField(max_length=20, default='', verbose_name='Mars'),
        ),
        migrations.AlterField(
            model_name='natal',
            name='mercury',
            field=models.CharField(max_length=20, default='', verbose_name='Mercury'),
        ),
        migrations.AlterField(
            model_name='natal',
            name='moon',
            field=models.CharField(max_length=20, default='', verbose_name='Moon'),
        ),
        migrations.AlterField(
            model_name='natal',
            name='neptun',
            field=models.CharField(max_length=20, default='', verbose_name='Neptun'),
        ),
        migrations.AlterField(
            model_name='natal',
            name='pluto',
            field=models.CharField(max_length=20, default='', verbose_name='Pluto'),
        ),
        migrations.AlterField(
            model_name='natal',
            name='saturn',
            field=models.CharField(max_length=20, default='', verbose_name='Saturn'),
        ),
        migrations.AlterField(
            model_name='natal',
            name='sun',
            field=models.CharField(max_length=20, default='', verbose_name='Sun'),
        ),
        migrations.AlterField(
            model_name='natal',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 6, 23, 1, 12, 672331, tzinfo=utc), verbose_name='Дата обновления'),
        ),
        migrations.AlterField(
            model_name='natal',
            name='uran',
            field=models.CharField(max_length=20, default='', verbose_name='Uran'),
        ),
        migrations.AlterField(
            model_name='natal',
            name='venus',
            field=models.CharField(max_length=20, default='', verbose_name='Venus'),
        ),
    ]
