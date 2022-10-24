from django.db import models

class Report(models.Model):
    idreport = models.AutoField(primary_key=True)
    iduser = models.ForeignKey('accounts.User', models.DO_NOTHING, db_column='idusuario', blank=True, null=True)
    idimage = models.ForeignKey('images.Image', models.DO_NOTHING, db_column='idimagem', blank=True, null=True)
    report= models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        db_table = 'report'
