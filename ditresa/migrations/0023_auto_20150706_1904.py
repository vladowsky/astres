# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ditresa', '0022_auto_20150706_1901'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Planet',
        ),
        migrations.DeleteModel(
            name='Zodiak',
        ),
        migrations.AlterField(
            model_name='natal',
            name='created_date',
            field=models.DateTimeField(verbose_name='Дата создания', default=datetime.datetime(2015, 7, 7, 0, 4, 12, 757389, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='natal',
            name='updated_date',
            field=models.DateTimeField(verbose_name='Дата обновления', default=datetime.datetime(2015, 7, 7, 0, 4, 12, 757389, tzinfo=utc)),
        ),
    ]
