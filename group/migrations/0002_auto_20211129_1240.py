# Generated by Django 3.2.9 on 2021-11-29 04:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='About',
            new_name='GAbout',
        ),
        migrations.RenameField(
            model_name='group',
            old_name='Media',
            new_name='GMedia',
        ),
        migrations.RenameField(
            model_name='group',
            old_name='Name',
            new_name='GName',
        ),
    ]
