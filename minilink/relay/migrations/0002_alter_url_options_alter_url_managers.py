# Generated by Django 5.0.3 on 2024-03-24 08:36

import django.db.models.manager
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('relay', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='url',
            options={'ordering': ('clicks',)},
        ),
        migrations.AlterModelManagers(
            name='url',
            managers=[
                ('popular', django.db.models.manager.Manager()),
            ],
        ),
    ]
