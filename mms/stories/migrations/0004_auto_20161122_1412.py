# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0003_auto_20161116_1908'),
    ]

    operations = [
        migrations.RenameField(
            model_name='story',
            old_name='story_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='story',
            old_name='story_instructions',
            new_name='instructions',
        ),
        migrations.RenameField(
            model_name='story',
            old_name='story_name',
            new_name='name',
        ),
    ]
