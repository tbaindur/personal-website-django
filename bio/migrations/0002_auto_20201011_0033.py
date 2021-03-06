# Generated by Django 3.1.2 on 2020-10-11 04:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experience',
            name='organization',
        ),
        migrations.AddField(
            model_name='experience',
            name='company',
            field=models.ForeignKey(default=0, limit_choices_to={'type.name': 'Company'}, on_delete=django.db.models.deletion.PROTECT, to='bio.organization'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='education',
            name='university',
            field=models.ForeignKey(limit_choices_to={'type.name': 'University'}, on_delete=django.db.models.deletion.PROTECT, to='bio.organization'),
        ),
    ]
