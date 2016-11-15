# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0005_auto_20161115_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='story_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 15, 20, 2, 34, 686000, tzinfo=utc), verbose_name=b'story date'),
        ),
        migrations.AlterField(
            model_name='response',
            name='submit_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 15, 20, 2, 34, 686000, tzinfo=utc), verbose_name=b'date submitted'),
        ),
        migrations.AlterField(
            model_name='waypoint',
            name='lat',
            field=models.DecimalField(default=0.0, max_digits=8, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='waypoint',
            name='lng',
            field=models.DecimalField(default=0.0, max_digits=8, decimal_places=5),
        ),
    ]
