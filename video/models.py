from django.db import models
import uuid

class Video(models.Model):
    idvideo = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    path = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    co_educator = models.ForeignKey('accounts.User', models.DO_NOTHING, db_column='codidusuario', blank=True, null=True)

    def __str__(self):
        return self.path
    class Meta:
        db_table = 'video'
