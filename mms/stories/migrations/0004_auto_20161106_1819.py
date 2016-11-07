# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0003_auto_20161025_1225'),
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
            ],
        ),
        migrations.AlterField(
            model_name='response',
            name='story_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 7, 0, 19, 0, 586000, tzinfo=utc), verbose_name=b'story date'),
        ),
        migrations.AlterField(
            model_name='response',
            name='submit_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 7, 0, 19, 0, 586000, tzinfo=utc), verbose_name=b'date submitted'),
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
