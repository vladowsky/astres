# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ditresa', '0028_auto_20150706_1912'),
    ]

    operations = [
        migrations.AddField(
            model_name='natal',
            name='jupiter',
            field=models.CharField(verbose_name='Jupiter', default='Zodiac', max_length=20),
        ),
        migrations.AddField(
            model_name='natal',
            name='mars',
            field=models.CharField(verbose_name='Mars', default='Zodiac', max_length=20),
        ),
        migrations.AddField(
            model_name='natal',
            name='mercury',
            field=models.CharField(verbose_name='Mercury', default='Zodiac', max_length=20),
        ),
        migrations.AddField(
            model_name='natal',
            name='moon',
            field=models.CharField(verbose_name='Moon', default='Zodiac', max_length=20),
        ),
        migrations.AddField(
            model_name='natal',
            name='neptun',
            field=models.CharField(verbose_name='Neptun', default='Zodiac', max_length=20),
        ),
        migrations.AddField(
            model_name='natal',
            name='pluto',
            field=models.CharField(verbose_name='Pluto', default='Zodiac', max_length=20),
        ),
        migrations.AddField(
            model_name='natal',
            name='saturn',
            field=models.CharField(verbose_name='Saturn', default='Zodiac', max_length=20),
        ),
        migrations.AddField(
            model_name='natal',
            name='sun',
            field=models.CharField(verbose_name='Sun', default='Zodiac', max_length=20),
        ),
        migrations.AddField(
            model_name='natal',
            name='uran',
            field=models.CharField(verbose_name='Uran', default='Zodiac', max_length=20),
        ),
        migrations.AddField(
            model_name='natal',
            name='venus',
            field=models.CharField(verbose_name='Venus', default='Zodiac', max_length=20),
        ),
        migrations.AlterField(
            model_name='natal',
            name='created_date',
            field=models.DateTimeField(verbose_name='Дата создания', default=datetime.datetime(2015, 7, 7, 1, 1, 41, 569629, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='natal',
            name='updated_date',
            field=models.DateTimeField(verbose_name='Дата обновления', default=datetime.datetime(2015, 7, 7, 1, 1, 41, 570629, tzinfo=utc)),
        ),
    ]
