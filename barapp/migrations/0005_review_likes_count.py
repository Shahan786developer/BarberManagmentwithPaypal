# Generated by Django 5.0.6 on 2024-06-14 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barapp', '0004_review_rew_date_alter_order_services_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='likes_count',
            field=models.IntegerField(default=0),
        ),
    ]