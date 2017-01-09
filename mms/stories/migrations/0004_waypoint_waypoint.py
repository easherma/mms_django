# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0003_auto_20170105_1544'),
    ]

    operations = [
        migrations.AddField(
            model_name='waypoint',
            name='waypoint',
            field=models.CharField(default='waypointsinit', max_length=200),
            preserve_default=False,
        ),
    ]
