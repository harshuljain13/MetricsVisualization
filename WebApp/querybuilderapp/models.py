# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class InfosysPricing(models.Model):
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    open_price = models.TextField(db_column='Open Price', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    high_price = models.TextField(db_column='High Price', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    low_price = models.TextField(db_column='Low Price', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    last_traded_price = models.TextField(db_column='Last Traded Price', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    close_price = models.TextField(db_column='Close Price', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    total_traded_quantity = models.TextField(db_column='Total Traded Quantity', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    turnover_in_lakhs_field = models.TextField(db_column='Turnover (in Lakhs)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'infosys_pricing'


class ReliancePricing(models.Model):
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    open_price = models.TextField(db_column='Open Price', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    high_price = models.TextField(db_column='High Price', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    low_price = models.TextField(db_column='Low Price', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    last_traded_price = models.TextField(db_column='Last Traded Price', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    close_price = models.TextField(db_column='Close Price', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    total_traded_quantity = models.TextField(db_column='Total Traded Quantity', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    turnover_in_lakhs_field = models.TextField(db_column='Turnover (in Lakhs)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'reliance_pricing'
