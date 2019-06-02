# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from .utils import MyModelDateField

class eod_hd(models.Model):
    Date = MyModelDateField(db_column='Date', null=False)
    Open = models.FloatField(db_column='Open', null=False)
    High = models.FloatField(db_column='High', null=False)
    Low = models.FloatField(db_column='Low', null=False)
    Close = models.FloatField(db_column='Close', null=False)
    Volume = models.FloatField(db_column='Volume', null=False)
    Dividend = models.FloatField(db_column='Dividend', null=False)
    Split = models.FloatField(db_column='Split', null=False)
    AdjOpen = models.FloatField(db_column='AdjOpen', null=False)
    AdjHigh = models.FloatField(db_column='AdjHigh', null=False)
    AdjLow = models.FloatField(db_column='AdjLow', null=False)
    AdjClose = models.FloatField(db_column='AdjClose', null=False)
    AdjVolume = models.FloatField(db_column='AdjVolume', null=False)
    
    class Meta:
        managed=True
        db_table = 'eod_hd'