# Generated by Django 3.2.9 on 2021-12-13 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0004_auto_20211211_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='Date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='Date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
