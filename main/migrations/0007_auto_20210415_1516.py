# Generated by Django 3.1.7 on 2021-04-15 14:16

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
