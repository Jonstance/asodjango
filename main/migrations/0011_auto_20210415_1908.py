# Generated by Django 3.1.7 on 2021-04-15 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20210415_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='bookImage',
            field=models.ImageField(upload_to='uploaded/'),
        ),
    ]