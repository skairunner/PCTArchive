# Generated by Django 2.1.5 on 2019-01-14 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snips', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='snip',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
