# Generated by Django 3.1.5 on 2022-10-15 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abbs', '0015_remove_papaabb_videourl'),
    ]

    operations = [
        migrations.AddField(
            model_name='papaabb',
            name='videourl',
            field=models.URLField(blank=True, null=True),
        ),
    ]
