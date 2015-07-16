# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ditresa', '0012_auto_20150706_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='natal',
            name='birth_date_time',
            field=models.DateTimeField(verbose_name='Дата рождения', default=datetime.datetime(2015, 7, 6, 18, 8, 9, 622714, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='natal',
            name='created_date',
            field=models.DateTimeField(verbose_name='Дата создания', default=datetime.datetime(2015, 7, 6, 18, 8, 9, 623715, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='natal',
            name='updated_date',
            field=models.DateTimeField(verbose_name='Дата обновления', default=datetime.datetime(2015, 7, 6, 18, 8, 9, 623715, tzinfo=utc)),
        ),
    ]
