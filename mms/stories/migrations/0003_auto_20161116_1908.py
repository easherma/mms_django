# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0002_auto_20161116_1906'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='story_id',
            new_name='story',
        ),
        migrations.RemoveField(
            model_name='submission',
            name='story_users_count',
        ),
    ]
