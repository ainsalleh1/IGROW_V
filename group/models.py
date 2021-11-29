from django.db import models, migrations
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib.syndication.views import Feed

# Create your models here.

class Group(models.Model):
    class Meta:
        db_table = 'Group'
    GName = models.CharField(max_length=150, null=True)
    GAbout = models.CharField(max_length=1000, null=True)
    GMedia = models.FileField(upload_to='uploads/',default="")

    def save(self):
        super().save()
        super().save(using='farming')
