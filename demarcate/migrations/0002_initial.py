# Generated by Django 4.1.2 on 2022-11-21 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('demarcate', '0001_initial'),
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='demarcate',
            name='idimage',
            field=models.ForeignKey(blank=True, db_column='idimagem', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='images.image'),
        ),
    ]
