# Generated by Django 2.0 on 2017-12-04 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_post_resume'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('bio', models.TextField()),
                ('image', models.ImageField(default='naruto.png', upload_to='images/')),
            ],
        ),
    ]