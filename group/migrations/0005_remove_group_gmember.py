# Generated by Django 3.2.9 on 2021-12-01 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0004_groupmember'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='GMember',
        ),
    ]
