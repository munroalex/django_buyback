"""Module for all SDE models relating directly to industry."""
from django.db import models

# Create your models here.


class Industryactivity(models.Model):
    """Model Class representing Industry Activities"""
    typeid = models.AutoField(db_column='typeID', primary_key=True)
    activityid = models.IntegerField(db_column='activityID')
    time = models.IntegerField(blank=True, null=True)

    class Meta:
        """Metadata Options"""
        managed = False
        db_table = 'industryActivity'
        unique_together = ['typeid', 'activityid']


class Industryactivitymaterials(models.Model):
    """Model Class representing Industry Activity Materials"""
    typeid = models.IntegerField(db_column='typeID', blank=True, null=True)
    activityid = models.IntegerField(
        db_column='activityID', blank=True, null=True)
    materialtypeid = models.IntegerField(
        db_column='materialTypeID', blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)

    class Meta:
        """Metadata Options"""
        managed = False
        db_table = 'industryActivityMaterials'


class Industryactivityprobabilities(models.Model):
    """Model Class representing Industry Activity Probabilities"""
    typeid = models.IntegerField(db_column='typeID', blank=True, null=True)
    activityid = models.IntegerField(
        db_column='activityID', blank=True, null=True)
    producttypeid = models.IntegerField(
        db_column='productTypeID', blank=True, null=True)
    probability = models.FloatField(blank=True, null=True)

    class Meta:
        """Metadata Options"""
        managed = False
        db_table = 'industryActivityProbabilities'


class Industryactivityproducts(models.Model):
    """Model Class representing Industry Activity Products"""
    typeid = models.IntegerField(db_column='typeID', blank=True, null=True)
    activityid = models.IntegerField(
        db_column='activityID', blank=True, null=True)
    producttypeid = models.IntegerField(
        db_column='productTypeID', blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)

    class Meta:
        """Metadata Options"""
        managed = False
        db_table = 'industryActivityProducts'


class Industryactivityskills(models.Model):
    """Model Class representing Industry Activity Skills"""
    typeid = models.IntegerField(db_column='typeID', blank=True, null=True)
    activityid = models.IntegerField(
        db_column='activityID', blank=True, null=True)
    skillid = models.IntegerField(db_column='skillID', blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)

    class Meta:
        """Metadata Options"""
        managed = False
        db_table = 'industryActivitySkills'


class Industryblueprints(models.Model):
    """Model Class representing Industry Blueprints"""
    typeid = models.AutoField(db_column='typeID', primary_key=True)
    maxproductionlimit = models.IntegerField(
        db_column='maxProductionLimit', blank=True, null=True)

    class Meta:
        """Metadata Options"""
        managed = False
        db_table = 'industryBlueprints'


class Ramactivities(models.Model):
    """Model Class representing Industry Activity Types"""
    activityid = models.AutoField(db_column='activityID', primary_key=True)
    activityname = models.CharField(
        db_column='activityName', blank=True, null=True, max_length=150)
    iconno = models.CharField(db_column='iconNo', blank=True, null=True, max_length=150)
    description = models.CharField(blank=True, null=True, max_length=150)
    published = models.BooleanField(blank=True, null=True)

    class Meta:
        """Metadata Options"""
        managed = False
        db_table = 'ramActivities'
