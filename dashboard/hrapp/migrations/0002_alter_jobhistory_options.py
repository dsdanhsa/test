# Generated by Django 5.0.4 on 2024-04-18 00:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jobhistory',
            options={'ordering': ['JOB_HISTORY_ID']},
        ),
    ]
