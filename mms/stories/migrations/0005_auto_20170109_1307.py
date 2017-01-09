# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0004_waypoint_waypoint'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='story',
            name='user',
        ),
        migrations.AddField(
            model_name='storyuser',
            name='story',
            field=models.ForeignKey(related_name='owner', to='stories.Story', null=True),
        ),
    ]
