# Generated by Django 4.1.2 on 2022-10-24 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0005_report_idimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='idimage',
        ),
    ]