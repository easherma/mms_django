# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0008_auto_20161122_1928'),
    ]

    operations = [
        migrations.AddField(
            model_name='storyuser',
            name='name',
            field=models.CharField(default='DEFAULT', max_length=200),
            preserve_default=False,
        ),
    ]
