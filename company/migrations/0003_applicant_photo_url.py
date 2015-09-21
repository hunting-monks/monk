# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_auto_20150917_0522'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='photo_url',
            field=models.CharField(default=b'', max_length=25, blank=True),
        ),
    ]
