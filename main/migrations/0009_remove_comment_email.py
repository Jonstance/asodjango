# Generated by Django 3.1.7 on 2021-04-15 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20210415_1543'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='email',
        ),
    ]
