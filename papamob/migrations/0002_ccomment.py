# Generated by Django 2.0.13 on 2020-12-17 07:12

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('papamob', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200, verbose_name='')),
                ('text', models.TextField(verbose_name='')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('approved_comment', models.BooleanField(default=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='papamob.PPost')),
            ],
        ),
    ]
