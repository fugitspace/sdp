# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='personcontacts',
            options={'verbose_name': 'person contact'},
        ),
        migrations.AlterModelOptions(
            name='personvitals',
            options={'verbose_name': 'vital'},
        ),
        migrations.AlterField(
            model_name='person',
            name='person_photo',
            field=models.ImageField(verbose_name='Passport Photo', blank=True, upload_to=''),
        ),
    ]
