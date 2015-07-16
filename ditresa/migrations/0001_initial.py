# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime
from django.utils.timezone import utc
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Natal',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('uuid', models.CharField(max_length=255, editable=False, default=uuid.uuid4, unique=True)),
                ('person', models.CharField(max_length=50, verbose_name='Имя записи')),
                ('birth_date_time', models.DateTimeField(verbose_name='Дата рождения', default=datetime.datetime(2015, 6, 8, 16, 2, 48, 32158, tzinfo=utc))),
                ('birth_place', models.CharField(max_length=255, verbose_name='Место рождения', default='London')),
                ('birth_latitude', models.FloatField(verbose_name='Широта рождения', default=55.75)),
                ('birth_longitude', models.FloatField(verbose_name='Долгота рождения', default=37.62)),
                ('sun', models.CharField(max_length=20, verbose_name='Sun')),
                ('moon', models.CharField(max_length=20, verbose_name='Moon')),
                ('mercury', models.CharField(max_length=20, verbose_name='Mercury')),
                ('venus', models.CharField(max_length=20, verbose_name='Venus')),
                ('mars', models.CharField(max_length=20, verbose_name='Mars')),
                ('jupiter', models.CharField(max_length=20, verbose_name='Jupiter')),
                ('saturn', models.CharField(max_length=20, verbose_name='Saturn')),
                ('uran', models.CharField(max_length=20, verbose_name='Uran')),
                ('neptun', models.CharField(max_length=20, verbose_name='Neptun')),
                ('pluto', models.CharField(max_length=20, verbose_name='Pluto')),
                ('created_date', models.DateTimeField(verbose_name='Дата создания', default=datetime.datetime(2015, 6, 8, 16, 2, 48, 32158, tzinfo=utc))),
                ('updated_date', models.DateTimeField(verbose_name='Дата обновления', default=datetime.datetime(2015, 6, 8, 16, 2, 48, 33158, tzinfo=utc))),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Persons',
                'ordering': ['-created_date'],
                'verbose_name': 'Person',
            },
        ),
    ]
