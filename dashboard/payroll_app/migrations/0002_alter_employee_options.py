# Generated by Django 5.0.4 on 2024-04-14 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payroll_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'ordering': ['idEmployee']},
        ),
    ]