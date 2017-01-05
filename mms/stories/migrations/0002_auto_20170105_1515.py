# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='user',
            field=models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, related_name='owner'),
        ),
        migrations.AlterField(
            model_name='submission',
            name='story',
            field=models.ForeignKey(to='stories.Story', related_name='submissions'),
        ),
        migrations.AlterField(
            model_name='submission',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='submissions'),
        ),
    ]
