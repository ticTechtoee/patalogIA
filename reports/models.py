from django.db import models
import uuid
class Report(models.Model):
    idreport = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    iduser = models.ForeignKey('accounts.User', models.DO_NOTHING, db_column='idusuario', blank=True, null=True)
    idimage = models.ForeignKey('images.Image', models.DO_NOTHING, db_column='idimagem', blank=True, null=True)
    report= models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        db_table = 'report'
