# Generated by Django 2.0 on 2017-12-04 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0026_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(default='value'),
            preserve_default=False,
        ),
    ]
