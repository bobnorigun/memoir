# Generated by Django 3.1.5 on 2021-01-21 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('abbs', '0002_book_genre'),
    ]

    operations = [
        migrations.RenameField(
            model_name='papaabb',
            old_name='summany',
            new_name='summary',
        ),
    ]