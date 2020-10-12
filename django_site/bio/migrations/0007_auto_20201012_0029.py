# Generated by Django 3.1.2 on 2020-10-12 04:29

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0006_auto_20201011_2050'),
    ]

    operations = [
        migrations.CreateModel(
            name='Intro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('headline', models.CharField(max_length=100)),
                ('summary', tinymce.models.HTMLField()),
                ('profile_pic', models.ImageField(default='profile_pics/default_profile_pic.jpg', upload_to='profile_pics')),
            ],
        ),
        migrations.AlterField(
            model_name='project',
            name='type',
            field=models.CharField(choices=[('Academic', 'Academic'), ('Professional', 'Professional'), ('Independent', 'Independent'), ('Hobby', 'Hobby')], max_length=20),
        ),
        migrations.AlterField(
            model_name='skill',
            name='proficiency_level',
            field=models.IntegerField(choices=[('Basic', 'Basic'), ('Intermediate', 'Intermediate'), ('Expert', 'Expert')], null=True),
        ),
    ]
