# Generated by Django 5.0.2 on 2024-03-14 12:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='worker',
        ),
        migrations.AddField(
            model_name='review',
            name='worker',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='barapp.worker'),
        ),
    ]
