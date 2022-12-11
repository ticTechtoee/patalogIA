from django.db import models
import uuid

class Forum(models.Model):
    idforum = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    data = models.DateField(blank=True, null=True)
    comments = models.CharField(max_length=250, blank=True, null=True)
    useriduser = models.ForeignKey('accounts.User', models.DO_NOTHING, db_column='usuarioidusuario', blank=True, null=True)

    class Meta:
        db_table = 'forum'
