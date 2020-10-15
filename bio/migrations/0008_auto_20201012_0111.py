# Generated by Django 3.1.2 on 2020-10-12 05:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bio', '0007_auto_20201012_0029'),
    ]

    operations = [
        migrations.AddField(
            model_name='intro',
            name='cover_pic',
            field=models.ImageField(null=True, upload_to='intro_pics'),
        ),
        migrations.AddField(
            model_name='intro',
            name='facebook_url',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='intro',
            name='github_url',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='intro',
            name='instagram_url',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='intro',
            name='linkedin_url',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='intro',
            name='resume',
            field=models.FileField(null=True, upload_to='docs'),
        ),
        migrations.AddField(
            model_name='intro',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='intro',
            name='profile_pic',
            field=models.ImageField(default='intro_pics/default_profile_pic.jpg', upload_to='intro_pics'),
        ),
    ]