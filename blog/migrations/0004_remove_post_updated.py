# Generated by Django 2.0.13 on 2019-11-05 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20191106_0222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='updated',
        ),
    ]
