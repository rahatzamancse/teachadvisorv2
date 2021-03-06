# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-28 15:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('school', models.CharField(max_length=120)),
                ('exam_type', models.CharField(max_length=120)),
                ('description', models.TextField(blank=True, null=True)),
                ('subject', models.CharField(max_length=120)),
                ('level', models.CharField(max_length=120)),
                ('publish', models.BooleanField(default=False)),
                ('docs', models.FileField(upload_to=b'')),
                ('creditcost', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TemporaryLink',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('user_agent', models.CharField(max_length=200)),
                ('user_ip', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('downloaded_at', models.DateTimeField()),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='temporarylinks', to='examdownload.Exam')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='temporarylinks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
