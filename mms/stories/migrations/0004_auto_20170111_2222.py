# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0003_auto_20170111_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='owner',
            field=models.ForeignKey(related_name='owner', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
