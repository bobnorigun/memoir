# Generated by Django 2.0.13 on 2021-01-19 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='profile',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
