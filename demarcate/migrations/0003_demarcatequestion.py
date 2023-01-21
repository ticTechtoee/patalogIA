# Generated by Django 4.1.2 on 2023-01-16 20:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('demarcate', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='demarcateQuestion',
            fields=[
                ('idmarks', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('x', models.IntegerField(blank=True, null=True)),
                ('y', models.IntegerField(blank=True, null=True)),
                ('w', models.IntegerField(blank=True, null=True)),
                ('h', models.IntegerField(blank=True, null=True)),
                ('area', models.IntegerField(blank=True, null=True)),
                ('questionImage', models.ImageField(blank=True, null=True, upload_to='question_images/')),
                ('question', models.CharField(max_length=500)),
            ],
        ),
    ]
