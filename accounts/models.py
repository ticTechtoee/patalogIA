from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    iduser = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)
    telephone = models.CharField(max_length=15, blank=True, null=True)
    usertype = models.ForeignKey('UserType', models.DO_NOTHING, db_column='codidtipousuario', blank=True, null=True)
    class Meta:
        db_table = 'user'

class UserType(models.Model):
    user_id= models.AutoField(primary_key=True)
    user_type= models.CharField(max_length=20, blank=True, null=True)
    def __str__(self):
        return self.user_type

    class Meta:
        db_table = 'user_type'
