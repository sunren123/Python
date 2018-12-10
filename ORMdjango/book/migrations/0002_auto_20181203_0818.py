# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book_Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('author', models.ForeignKey(to='book.Author')),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='authors',
        ),
        migrations.AddField(
            model_name='book_author',
            name='book',
            field=models.ForeignKey(to='book.Book'),
        ),
    ]
