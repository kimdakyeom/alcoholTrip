# Generated by Django 3.2.13 on 2022-11-01 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bars', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='like_users',
        ),
    ]