# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    replaces = [(b'stories', '0001_initial'), (b'stories', '0002_auto_20161025_1159'), (b'stories', '0003_auto_20161025_1225'), (b'stories', '0004_auto_20161106_1819'), (b'stories', '0005_auto_20161115_1359'), (b'stories', '0006_auto_20161115_1402'), (b'stories', '0007_auto_20161115_1404'), (b'stories', '0008_auto_20161115_1407')]

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('story_name', models.CharField(max_length=200)),
                ('story_description', models.TextField()),
                ('story_instructions', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('story_users_count', models.IntegerField(default=0)),
                ('story_id', models.ForeignKey(to='stories.Story')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(max_length=200)),
                ('user_email', models.EmailField(max_length=254)),
                ('story_id', models.ForeignKey(to='stories.Story')),
            ],
        ),
        migrations.CreateModel(
            name='Waypoint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('geom', models.CharField(max_length=200)),
                ('notes', models.TextField()),
                ('path_order', models.IntegerField(default=0)),
                ('lat', models.DecimalField(max_digits=8, decimal_places=5)),
                ('lng', models.DecimalField(max_digits=8, decimal_places=5)),
            ],
        ),
        migrations.AddField(
            model_name='submission',
            name='user_id',
            field=models.ForeignKey(to='stories.User'),
        ),
        migrations.AddField(
            model_name='submission',
            name='waypoint_id',
            field=models.ForeignKey(to='stories.Waypoint'),
        ),
    ]
