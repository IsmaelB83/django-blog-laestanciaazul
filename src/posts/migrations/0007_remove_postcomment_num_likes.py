# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-15 05:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [('posts', '0006_post_num_likes'), ]

    operations = [migrations.RemoveField(model_name='postcomment', name='num_likes', ), ]
