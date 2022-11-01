# Generated by Django 4.1.2 on 2022-10-24 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
        ('reports', '0004_remove_report_idimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='idimage',
            field=models.ForeignKey(blank=True, db_column='idimagem', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='images.image'),
        ),
    ]