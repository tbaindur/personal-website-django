# Generated by Django 3.1.2 on 2020-10-12 00:50

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0005_auto_20201011_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='details',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='experience',
            name='details',
            field=tinymce.models.HTMLField(),
        ),
    ]