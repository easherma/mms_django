# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prompt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('prompt_text', models.CharField(max_length=200)),
                ('create_date', models.DateTimeField(verbose_name=b'date created')),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('response_text', models.CharField(max_length=200)),
                ('count', models.IntegerField(default=0)),
                ('question', models.ForeignKey(to='stories.Prompt')),
            ],
        ),
    ]
