# Generated by Django 2.0.13 on 2021-01-19 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_author_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='bookcover',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
