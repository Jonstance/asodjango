# Generated by Django 3.1.7 on 2021-04-13 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_blog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='bookAmount',
        ),
        migrations.AddField(
            model_name='books',
            name='bookLink',
            field=models.URLField(blank=True),
        ),
    ]
