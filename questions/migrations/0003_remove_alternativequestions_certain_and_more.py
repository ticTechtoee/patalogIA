# Generated by Django 4.1.2 on 2022-12-11 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_alter_questions_codimage_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alternativequestions',
            name='certain',
        ),
        migrations.AddField(
            model_name='questions',
            name='certain',
            field=models.CharField(blank=True, default='A', max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='alternativequestions',
            name='questoes_questoes_id',
            field=models.ForeignKey(db_column='questoes_idquestoes', on_delete=django.db.models.deletion.DO_NOTHING, to='questions.questions', verbose_name='Related Question'),
        ),
    ]
