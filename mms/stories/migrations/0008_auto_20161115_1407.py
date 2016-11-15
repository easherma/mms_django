# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0007_auto_20161115_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='waypoint',
            name='lat',
            field=models.DecimalField(max_digits=8, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='waypoint',
            name='lng',
            field=models.DecimalField(max_digits=8, decimal_places=5),
        ),
    ]
