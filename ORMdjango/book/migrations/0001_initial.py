# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField(max_length=20, default=20)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('pub_date', models.DateTimeField()),
                ('authors', models.ManyToManyField(to='book.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Publish',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='publish',
            field=models.ForeignKey(to='book.Publish'),
        ),
    ]
