# Generated by Django 4.1.2 on 2022-10-24 06:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('video', '0004_delete_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('idvideo', models.AutoField(primary_key=True, serialize=False)),
                ('path', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('co_educator', models.ForeignKey(blank=True, db_column='codidusuario', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'video',
            },
        ),
    ]