# Generated by Django 2.0 on 2017-12-03 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='media/naruto.png', upload_to='media/'),
        ),
    ]
