# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-16 14:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [('posts', '0013_auto_20171216_1502'), ]

    operations = [migrations.RenameField(model_name='postcomment', old_name='annonymous_email', new_name='anonymous_email', ),
        migrations.RenameField(model_name='postcomment', old_name='annonymous_name', new_name='anonymous_name', ), ]
