# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='submission',
            old_name='story_id',
            new_name='story',
        ),
        migrations.RenameField(
            model_name='submission',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='submission',
            name='waypoint_id',
        ),
        migrations.AddField(
            model_name='waypoint',
            name='submission',
            field=models.ForeignKey(to='stories.Submission', null=True),
        ),
    ]
