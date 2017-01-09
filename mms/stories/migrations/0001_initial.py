# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('instructions', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('story', models.ForeignKey(related_name='submissions', to='stories.Story')),
                ('user', models.ForeignKey(related_name='submissions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Waypoint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('waypoint', models.CharField(max_length=200)),
                ('geom', models.CharField(max_length=200)),
                ('notes', models.TextField()),
                ('lng', models.DecimalField(max_digits=8, decimal_places=5)),
                ('lat', models.DecimalField(max_digits=8, decimal_places=5)),
                ('path_order', models.IntegerField(default=0)),
                ('submission', models.ForeignKey(related_name='waypoints', to='stories.Submission', null=True)),
            ],
        ),
    ]
