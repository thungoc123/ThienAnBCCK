# Generated by Django 4.1.7 on 2023-07-08 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myhome', '0003_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='subtitle',
            field=models.TextField(default='null'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='null', upload_to='upload/'),
        ),
    ]