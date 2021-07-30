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
    timestamp = models.IntegerField()
    user_iduser = models.ForeignKey('User', models.DO_NOTHING, db_column='user_iduser')
    ammount = models.FloatField(blank=True)

    class Meta:
        managed = False
        db_table = 'record'


class Type(models.Model):
    idtype = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'type'


class User(models.Model):
    iduser = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'user'
