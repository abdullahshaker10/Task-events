# Generated by Django 3.1.5 on 2021-01-24 22:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20210124_1536'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ('date',)},
        ),
    ]
