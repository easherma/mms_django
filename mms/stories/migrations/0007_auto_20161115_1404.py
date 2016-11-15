# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0006_auto_20161115_1402'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='response',
            name='prompt',
        ),
        migrations.DeleteModel(
            name='Prompt',
        ),
        migrations.DeleteModel(
            name='Response',
        ),
    ]
