from django.db import models


class Video(models.Model):
    idvideo = models.AutoField(primary_key=True)
    path = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    co_educator = models.ForeignKey('accounts.User', models.DO_NOTHING, db_column='codidusuario', blank=True, null=True)

    def __str__(self):
        return self.path
    class Meta:
        db_table = 'video'
