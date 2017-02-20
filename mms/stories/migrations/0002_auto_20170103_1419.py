# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='story',
            field=models.ForeignKey(related_name='submissions', to='stories.Story'),
        ),
    ]
