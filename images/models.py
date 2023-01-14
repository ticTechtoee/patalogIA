from django.db import models
import uuid

class Image(models.Model):
    idimage = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    path = models.CharField(max_length=250, blank=True, null=True)
    question_image = models.ImageField(upload_to='question_images/', null=True, blank=True)
    dataimg = models.DateTimeField(blank=True, null=True)
    codtype_picture = models.ForeignKey('ImageType', models.DO_NOTHING, db_column='codtipoimagem', blank=True, null=True)
    useriduser = models.ForeignKey('accounts.User', models.DO_NOTHING, db_column='usuarioidusuario', blank=True, null=True)
    specialtydespecialty = models.ForeignKey('Specialty', models.DO_NOTHING, db_column='especialidadeidespecialidade', blank=True, null=True)
    
    class Meta:
        db_table = 'image'


class ImageType(models.Model):
    id_type_image = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    description = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'image_type'

class ImagesQuestions(models.Model):
    idimages_questions = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    daterecord = models.DateTimeField(blank=True, null=True)
    id_image = models.ForeignKey(Image, models.DO_NOTHING, db_column='id_imagem', blank=True, null=True)
    id_quest = models.ForeignKey('questions.Questions', models.DO_NOTHING, db_column='id_questao', blank=True, null=True)

    class Meta:
        db_table = 'images_questions'


# Temp

class Specialty(models.Model):
    idespecialty = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    description = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'specialty'

