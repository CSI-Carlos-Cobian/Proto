# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Record(models.Model):
    idrecord = models.AutoField(primary_key=True)
    type_idtype = models.ForeignKey('Type', models.DO_NOTHING, db_column='type_idtype')
    timestamp = models.PositiveBigIntegerField()
    user_iduser = models.ForeignKey('User', models.DO_NOTHING, db_column='user_iduser')
    ammount = models.FloatField(blank=True)

    # def __init__(self, idrecord:int, type_idtype, timestamp, user_iduser, ammount:float, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.idrecord:int = idrecord
    #     self.type_idtype:Type = Type(type_idtype)
    #     self.timestamp:int = int.from_bytes(timestamp, 
    #                                         byteorder='big', 
    #                                         signed=False)
    #     self.user_iduser:User = User(user_iduser)
    #     self.ammount:float = ammount

    class Meta:
        managed = False
        db_table = 'Record'


class Type(models.Model):
    idtype = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45)

    # def __init__(self, idtype, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.idtype:int = int.from_bytes(   idtype, 
    #                                         byteorder='big', 
    #                                         signed=False)
    #     self.name:str = Type.getTypeName(idtype)

    def getTypeName(idType):
        type = {
            b'\x00': "Debit",
            b'\x01': "Credit",
            b'\x02': "StartAutopay",
            b'\x03': "EndAutopay"
        }
        return type.get(idType, "Invalid State")

    def hasField(idType):
        type = {
            b'\x00': True,
            b'\x01': True,
            b'\x02': False,
            b'\x03': False
        }
        return type.get(idType, "Invalid State")
    class Meta:
        managed = False
        db_table = 'Type'


class User(models.Model):
    iduser = models.PositiveBigIntegerField(primary_key=True)

    # def __init__(self, iduser, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.iduser = int.from_bytes(   iduser, 
    #                                     byteorder='big', 
    #                                     signed=False)

    class Meta:
        managed = False
        db_table = 'User'
