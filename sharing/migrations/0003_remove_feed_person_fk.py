# Generated by Django 3.2.9 on 2022-01-16 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sharing', '0002_auto_20220117_0137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feed',
            name='Person_fk',
        ),
    ]