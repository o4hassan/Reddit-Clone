# Generated by Django 2.0 on 2017-12-03 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_auto_20171203_0416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to='media/resumes/'),
        ),
    ]
