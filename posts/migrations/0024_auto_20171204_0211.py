# Generated by Django 2.0 on 2017-12-04 02:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0023_auto_20171204_0207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(default=0, on_delete=None, to=settings.AUTH_USER_MODEL),
        ),
    ]
