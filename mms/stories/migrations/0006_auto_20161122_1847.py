# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0005_auto_20161122_1432'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='story',
        ),
        migrations.AddField(
            model_name='story',
            name='user',
            field=models.ForeignKey(to='stories.User', null=True),
        ),
    ]
