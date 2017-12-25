# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-25 10:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import user.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('location', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
                ('image', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=user.models.upload_location_author, width_field='width_field')),
                ('image_url', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
