# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0002_story_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='waypoint',
            name='gid',
            field=models.TextField(default='gid'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='waypoint',
            name='label',
            field=models.TextField(default='label'),
            preserve_default=False,
        ),
    ]
