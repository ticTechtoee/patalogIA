from django.db import models

class demarcate(models.Model):
    idmarks = models.AutoField(primary_key=True)
    x = models.IntegerField(blank=True, null=True)
    y = models.IntegerField(blank=True, null=True)
    w = models.IntegerField(blank=True, null=True)
    h = models.IntegerField(blank=True, null=True)
    right = models.IntegerField(blank=True, null=True)
    bottom = models.IntegerField(blank=True, null=True)
    area = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    idimage = models.ForeignKey('images.Image', models.DO_NOTHING, db_column='idimagem', blank=True, null=True)

    class Meta:
        db_table = 'demarcate'
