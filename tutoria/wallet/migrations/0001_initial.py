# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-23 14:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        ('scheduler', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('code', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduler.BookingRecord')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField()),
                ('issuer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issuer', to='account.User')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='account.User')),
            ],
        ),
    ]
