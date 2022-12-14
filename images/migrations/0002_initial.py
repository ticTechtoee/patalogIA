# Generated by Django 4.1.2 on 2022-11-21 08:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('questions', '0001_initial'),
        ('images', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='imagesquestions',
            name='id_quest',
            field=models.ForeignKey(blank=True, db_column='id_questao', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='questions.questions'),
        ),
        migrations.AddField(
            model_name='image',
            name='codtype_picture',
            field=models.ForeignKey(blank=True, db_column='codtipoimagem', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='images.imagetype'),
        ),
        migrations.AddField(
            model_name='image',
            name='specialtydespecialty',
            field=models.ForeignKey(blank=True, db_column='especialidadeidespecialidade', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='images.specialty'),
        ),
        migrations.AddField(
            model_name='image',
            name='useriduser',
            field=models.ForeignKey(blank=True, db_column='usuarioidusuario', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
