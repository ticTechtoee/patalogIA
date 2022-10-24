from django.db import models

class Questions(models.Model):
    idquestions = models.AutoField(primary_key=True)
    question = models.IntegerField(db_column='questaoNum', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(max_length=150, blank=True, null=True)
    value = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    typequestionandidtypequestion = models.ForeignKey('QuestionTypes', models.DO_NOTHING, db_column='tipoquestoesidtipoquestoes', blank=True, null=True)
    questionnaireidquestionnaire = models.ForeignKey('Questionnaire', models.DO_NOTHING, db_column='questionarioidquestionario', blank=True, null=True)
    videoidvideo = models.ForeignKey('video.Video', models.DO_NOTHING, db_column='videoidvideo', blank=True, null=True)
    codimage = models.ForeignKey('images.Image', models.DO_NOTHING, db_column='codimagem', blank=True, null=True)

    class Meta:
        db_table = 'questions'

class AlternativeQuestions(models.Model):
    idquestions_alternatives = models.AutoField(primary_key=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    letter = models.CharField(max_length=1, blank=True, null=True)
    certain = models.CharField(max_length=1, blank=True, null=True)
    questoes_questoes_id = models.ForeignKey('Questions', models.DO_NOTHING, db_column='questoes_idquestoes', blank=True, null=True)

    class Meta:
        db_table = 'alternative_questions'

class QuestionTypes(models.Model):
    idtype_questions = models.AutoField(primary_key=True)
    category = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        db_table = 'question_types'

class Questionnaire(models.Model):
    idquestionnaire = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150, blank=True, null=True)
    Subject = models.CharField(max_length=250, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    quests = models.IntegerField(blank=True, null=True)
    #Co Educator This Feild needs to be addressed
    co_educator = models.ForeignKey('accounts.User', models.DO_NOTHING, db_column='codidusuario', blank=True, null=True)
    usercode = models.ForeignKey('accounts.UserType', models.DO_NOTHING, db_column='codtipousuario', blank=True, null=True)

    class Meta:
        db_table = 'questionnaire'




class Result(models.Model):
    idresult = models.AutoField(primary_key=True)
    iduser_user = models.ForeignKey('accounts.User', models.DO_NOTHING, db_column='usuario_idusuario', blank=True, null=True)
    quiz_quiz_id = models.ForeignKey('Questionnaire', models.DO_NOTHING, db_column='questionario_idquestionario', blank=True, null=True)
    descriptiondate = models.DateTimeField(blank=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        db_table = 'result'


# Temp
class Cases(models.Model):
    idcase = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=250, blank=True, null=True)
    imageidimage = models.ForeignKey('images.Image', models.DO_NOTHING, db_column='imagemidimagem', blank=True, null=True)
    # This Needs to be Discussed
    this_question = models.ForeignKey('Questions', models.DO_NOTHING, db_column='questoesidquestao', blank=True, null=True)
    useriduser = models.ForeignKey('accounts.User', models.DO_NOTHING, db_column='usuarioidusuario', blank=True, null=True)

    class Meta:
        db_table = 'cases'


