# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ditresa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='natal',
            name='birth_date_time',
            field=models.DateTimeField(verbose_name='Дата рождения', default=datetime.datetime(2015, 6, 8, 16, 9, 40, 613136, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='natal',
            name='created_date',
            field=models.DateTimeField(verbose_name='Дата создания', default=datetime.datetime(2015, 6, 8, 16, 9, 40, 614136, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='natal',
            name='updated_date',
            field=models.DateTimeField(verbose_name='Дата обновления', default=datetime.datetime(2015, 6, 8, 16, 9, 40, 614136, tzinfo=utc)),
        ),
    ]
