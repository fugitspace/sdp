# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(verbose_name='Sex', max_length=255)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MaritalStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'marital status',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(verbose_name='First name', max_length=255)),
                ('surname', models.CharField(verbose_name='Surname', max_length=255)),
                ('othername', models.CharField(verbose_name='Othername', blank=True, max_length=255)),
                ('home_village', models.CharField(verbose_name='Home Village', blank=True, max_length=255)),
                ('person_photo', models.FilePathField(verbose_name='Passport Photo', blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'persons',
                'ordering': ['first_name', 'surname'],
            },
        ),
        migrations.CreateModel(
            name='PersonContacts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('telephone', models.CharField(verbose_name='Telephone (Mobile)', blank=True, max_length=255)),
                ('mailing_address', models.CharField(verbose_name='Mailing Address', blank=True, max_length=255)),
                ('residence', models.CharField(blank=True, max_length=255)),
                ('person', models.ForeignKey(to='person.Person')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PersonDemographic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('date_of_birth', models.DateField(blank=True)),
                ('gender', models.ForeignKey(blank=True, to='person.Gender')),
                ('marital_status', models.ForeignKey(blank=True, to='person.MaritalStatus')),
                ('person', models.ForeignKey(to='person.Person')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'demographic',
            },
        ),
        migrations.CreateModel(
            name='PersonGuardian',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('father_name', models.CharField(verbose_name="Father's Name", blank=True, max_length=255)),
                ('mother_name', models.CharField(verbose_name="Mother's Name", blank=True, max_length=255)),
                ('guardian_occupation', models.CharField(blank=True, max_length=255)),
                ('person', models.ForeignKey(to='person.Person')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'guardian/next of kin',
            },
        ),
        migrations.CreateModel(
            name='PersonVitals',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('body_temperature', models.FloatField(blank=True, help_text='Temperature in Degrees Celcius')),
                ('blood_pressure', models.FloatField(blank=True)),
                ('weight', models.FloatField(blank=True)),
                ('person', models.ForeignKey(to='person.Person')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'vitals',
            },
        ),
    ]
