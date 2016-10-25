# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0002_auto_20161025_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='response',
            name='story_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 25, 17, 25, 38, 349000, tzinfo=utc), verbose_name=b'story date'),
        ),
        migrations.AddField(
            model_name='response',
            name='submit_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 25, 17, 25, 38, 349000, tzinfo=utc), verbose_name=b'date submitted'),
        ),
    ]
