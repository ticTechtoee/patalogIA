from django.db import models


class Forum(models.Model):
    idforum = models.AutoField(primary_key=True)
    data = models.DateField(blank=True, null=True)
    comments = models.CharField(max_length=250, blank=True, null=True)
    useriduser = models.ForeignKey('accounts.User', models.DO_NOTHING, db_column='usuarioidusuario', blank=True, null=True)

    class Meta:
        db_table = 'forum'
