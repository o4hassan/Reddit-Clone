# Generated by Django 2.0 on 2017-12-03 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_auto_20171203_0418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='naruto.png', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to='resumes/'),
        ),
    ]
