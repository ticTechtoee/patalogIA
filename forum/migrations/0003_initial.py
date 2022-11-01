# Generated by Django 4.1.2 on 2022-10-24 07:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0002_delete_forum'),
    ]

    operations = [
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('idforum', models.AutoField(primary_key=True, serialize=False)),
                ('data', models.DateField(blank=True, null=True)),
                ('comments', models.CharField(blank=True, max_length=250, null=True)),
                ('useriduser', models.ForeignKey(blank=True, db_column='usuarioidusuario', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'forum',
            },
        ),
    ]