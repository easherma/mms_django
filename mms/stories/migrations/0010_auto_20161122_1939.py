# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0009_storyuser_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='storyuser',
            old_name='name',
            new_name='username',
        ),
    ]
