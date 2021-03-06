# Generated by Django 3.2.9 on 2022-01-16 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0006_alter_person_photo'),
        ('sharing', '0004_feed_person_fk'),
        ('group', '0011_auto_20211211_0133'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='Feed_fk',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sharing.feed'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='GProfile',
            field=models.FileField(default='', upload_to='media/'),
        ),
        migrations.AddField(
            model_name='group',
            name='Person_fk',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='member.person'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='group',
            name='GMedia',
            field=models.FileField(default='', upload_to='media/'),
        ),
    ]
