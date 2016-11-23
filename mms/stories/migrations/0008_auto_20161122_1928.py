# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0007_auto_20161122_1908'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoryUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('email', models.EmailField(unique=True, max_length=254)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='story',
            name='user',
            field=models.ForeignKey(to='stories.StoryUser', null=True),
        ),
        migrations.AlterField(
            model_name='submission',
            name='user',
            field=models.ForeignKey(to='stories.StoryUser'),
        ),
    ]
