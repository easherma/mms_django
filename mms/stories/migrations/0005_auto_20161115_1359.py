# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0004_auto_20161106_1819'),
    ]

    operations = [
        migrations.AddField(
            model_name='waypoint',
            name='lat',
            field=models.DecimalField(default=datetime.datetime(2016, 11, 15, 19, 58, 6, 999000, tzinfo=utc), max_digits=8, decimal_places=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='waypoint',
            name='lng',
            field=models.DecimalField(default=0.0, max_digits=8, decimal_places=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='response',
            name='story_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 15, 19, 57, 25, 533000, tzinfo=utc), verbose_name=b'story date'),
        ),
        migrations.AlterField(
            model_name='response',
            name='submit_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 15, 19, 57, 25, 532000, tzinfo=utc), verbose_name=b'date submitted'),
        ),
    ]
