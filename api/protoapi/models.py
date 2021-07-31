from __future__ import unicode_literals
from django.db import models

class Type(models.Model):
    idtype = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45)

    def getTypeName(idBytes):
        type = {
            b'\x00': "Debit",
            b'\x01': "Credit",
            b'\x02': "StartAutopay",
            b'\x03': "EndAutopay"
        }
        return type.get(idBytes, "Invalid State")

    def hasField(idBytes):
        type = {
            b'\x00': True,
            b'\x01': True,
            b'\x02': False,
            b'\x03': False
        }
        return type.get(idBytes, "Invalid State")
    class Meta:
        managed = False
        db_table = 'type'


class User(models.Model):
    iduser = models.PositiveBigIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'user'

class Record(models.Model):
    idrecord = models.AutoField(primary_key=True)
    type_idtype = models.ForeignKey(Type, models.DO_NOTHING, db_column='type_idtype')
    timestamp = models.PositiveBigIntegerField()
    user_iduser = models.ForeignKey(User, models.DO_NOTHING, db_column='user_iduser')
    ammount = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'record'