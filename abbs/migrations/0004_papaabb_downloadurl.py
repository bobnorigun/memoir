# Generated by Django 3.1.5 on 2021-01-22 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abbs', '0003_auto_20210121_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='papaabb',
            name='downloadurl',
            field=models.URLField(blank=True, null=True),
        ),
    ]
