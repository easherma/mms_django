# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0002_auto_20170105_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='waypoint',
            name='submission',
            field=models.ForeignKey(to='stories.Submission', null=True, related_name='waypoints'),
        ),
    ]
