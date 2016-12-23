# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-06 18:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import eventtools.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('isubscribe', '0008_auto_20161105_1457'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventMembers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Event Member',
                'ordering': ['order'],
                'verbose_name_plural': 'Event Member',
            },
        ),
        migrations.CreateModel(
            name='ScheduledEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.IntegerField(choices=[(0, 'On Duty'), (1, 'Do Not Disturb')])),
                ('description', models.CharField(blank=True, max_length=128, null=True)),
                ('members', models.ManyToManyField(related_name='members', through='isubscribe.EventMembers', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Scheduled Event',
                'ordering': ['event'],
                'verbose_name_plural': 'Scheduled Events',
            },
            bases=(models.Model, eventtools.models.OccurrenceMixin),
        ),
        migrations.CreateModel(
            name='ScheduledOccurrence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField(db_index=True)),
                ('end', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('repeat', eventtools.models.ChoiceTextField(blank=True, choices=[('RRULE:FREQ=DAILY', 'Daily'), ('RRULE:FREQ=WEEKLY', 'Weekly'), ('RRULE:FREQ=MONTHLY', 'Monthly'), ('RRULE:FREQ=YEARLY', 'Yearly')], default='')),
                ('repeat_until', models.DateField(blank=True, null=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='isubscribe.ScheduledEvent')),
            ],
            options={
                'verbose_name': 'Scheduled Occurrence',
                'verbose_name_plural': 'Scheduled Occurrences',
            },
            bases=(models.Model, eventtools.models.OccurrenceMixin),
        ),
        migrations.AddField(
            model_name='eventmembers',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='isubscribe.ScheduledEvent'),
        ),
        migrations.AddField(
            model_name='eventmembers',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]