# Generated by Django 4.1.7 on 2023-06-17 03:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myhome', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Topic',
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='comment',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
