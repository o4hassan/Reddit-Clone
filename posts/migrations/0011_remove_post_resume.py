# Generated by Django 2.0 on 2017-12-03 05:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_auto_20171203_0419'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='resume',
        ),
    ]