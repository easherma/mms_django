# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

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
                ('lng', models.DecimalField(max_digits=8, decimal_places=5)),
                ('lat', models.DecimalField(max_digits=8, decimal_places=5)),
                ('path_order', models.IntegerField(default=0)),
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
