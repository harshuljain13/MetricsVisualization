# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class vizpoc(models.Model):
    UtilityName = models.TextField(db_column='UtilityName')  # Field name made lowercase.
    StateName = models.TextField(db_column='StateName')  # Field name made lowercase.
    CountyName = models.TextField(db_column='CountyName')  # Field name made lowercase.
    OutageCount = models.IntegerField(db_column='OutageCount', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    CustomerCount = models.IntegerField(db_column='CustomerCount', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    RecordDateTime = models.DateTimeField(db_column='RecordDateTime')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    StepCount = models.IntegerField(db_column='StepCount', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    PerDiff = models.FloatField(db_column='PerDiff', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    Duration = models.FloatField(db_column='Duration', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    
    class Meta:
        unique_together = (('UtilityName', 'StateName', 'CountyName', 'RecordDateTime'))
        managed = True
        db_table = 'vizpoc'
        