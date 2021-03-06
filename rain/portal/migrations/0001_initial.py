# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-10 13:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Interaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('views', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='RNA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=128, unique=True)),
                ('description', models.TextField()),
                ('views', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='interaction',
            name='entity1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entity1', to='portal.RNA'),
        ),
        migrations.AddField(
            model_name='interaction',
            name='entity2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entity2', to='portal.RNA'),
        ),
    ]
