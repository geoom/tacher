# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_auto_20141004_1033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='average_record',
        ),
    ]
