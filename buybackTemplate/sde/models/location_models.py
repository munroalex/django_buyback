"""Module for all SDE models relating directly to locations."""
from django.db import models

# Create your models here.


class Stastations(models.Model):
    """Model Class representing NPC Stations"""
    stationid = models.AutoField(db_column='stationID', primary_key=True)
    security = models.FloatField(blank=True, null=True)
    dockingcostpervolume = models.FloatField(
        db_column='dockingCostPerVolume', blank=True, null=True)
    maxshipvolumedockable = models.FloatField(
        db_column='maxShipVolumeDockable', blank=True, null=True)
    officerentalcost = models.IntegerField(
        db_column='officeRentalCost', blank=True, null=True)
    operationid = models.IntegerField(
        db_column='operationID', blank=True, null=True)
    stationtypeid = models.IntegerField(
        db_column='stationTypeID', blank=True, null=True)
    corporationid = models.IntegerField(
        db_column='corporationID', blank=True, null=True)
    solarsystemid = models.IntegerField(
        db_column='solarSystemID', blank=True, null=True)
    constellationid = models.IntegerField(
        db_column='constellationID', blank=True, null=True)
    regionid = models.IntegerField(db_column='regionID', blank=True, null=True)
    stationname = models.CharField(
        db_column='stationName', blank=True, null=True)
    x = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)
    z = models.FloatField(blank=True, null=True)
    reprocessingefficiency = models.FloatField(
        db_column='reprocessingEfficiency', blank=True, null=True)
    reprocessingstationstake = models.FloatField(
        db_column='reprocessingStationsTake', blank=True, null=True)
    reprocessinghangarflag = models.IntegerField(
        db_column='reprocessingHangarFlag', blank=True, null=True)

    class Meta:
        """Metadata Options"""
        managed = False
        db_table = 'staStations'


class Mapsolarsystems(models.Model):
    """Model Class representing Solar Systems"""
    regionid = models.IntegerField(db_column='regionID', blank=True, null=True)
    constellationid = models.IntegerField(
        db_column='constellationID', blank=True, null=True)
    solarsystemid = models.AutoField(
        db_column='solarSystemID', primary_key=True)
    solarsystemname = models.CharField(
        db_column='solarSystemName', blank=True, null=True)
    x = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)
    z = models.FloatField(blank=True, null=True)
    xmin = models.FloatField(db_column='xMin', blank=True, null=True)
    xmax = models.FloatField(db_column='xMax', blank=True, null=True)
    ymin = models.FloatField(db_column='yMin', blank=True, null=True)
    ymax = models.FloatField(db_column='yMax', blank=True, null=True)
    zmin = models.FloatField(db_column='zMin', blank=True, null=True)
    zmax = models.FloatField(db_column='zMax', blank=True, null=True)
    luminosity = models.FloatField(blank=True, null=True)
    border = models.BooleanField(blank=True, null=True)
    fringe = models.BooleanField(blank=True, null=True)
    corridor = models.BooleanField(blank=True, null=True)
    hub = models.BooleanField(blank=True, null=True)
    international = models.BooleanField(blank=True, null=True)
    regional = models.BooleanField(blank=True, null=True)
    constellation = models.BooleanField(blank=True, null=True)
    security = models.FloatField(blank=True, null=True)
    factionid = models.IntegerField(
        db_column='factionID', blank=True, null=True)
    radius = models.FloatField(blank=True, null=True)
    suntypeid = models.IntegerField(
        db_column='sunTypeID', blank=True, null=True)
    securityclass = models.CharField(
        db_column='securityClass', blank=True, null=True)

    class Meta:
        """Metadata Options"""
        managed = False
        db_table = 'mapSolarSystems'


class Mapsolarsystemjumps(models.Model):
    """Model Class representing Solar System Jumps"""
    fromregionid = models.IntegerField(
        db_column='fromRegionID', blank=True, null=True)
    fromconstellationid = models.IntegerField(
        db_column='fromConstellationID', blank=True, null=True)
    fromsolarsystemid = models.AutoField(
        db_column='fromSolarSystemID', primary_key=True)
    tosolarsystemid = models.IntegerField(db_column='toSolarSystemID')
    toconstellationid = models.IntegerField(
        db_column='toConstellationID', blank=True, null=True)
    toregionid = models.IntegerField(
        db_column='toRegionID', blank=True, null=True)

    class Meta:
        """Metadata Options"""
        managed = False
        db_table = 'mapSolarSystemJumps'
        unique_together = ['fromSolarSystemID', 'toSolarSystemID']


class Mapregions(models.Model):
    """Model Class representing Regions"""
    regionid = models.AutoField(db_column='regionID', primary_key=True)
    regionname = models.CharField(
        db_column='regionName', blank=True, null=True)
    x = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)
    z = models.FloatField(blank=True, null=True)
    xmin = models.FloatField(db_column='xMin', blank=True, null=True)
    xmax = models.FloatField(db_column='xMax', blank=True, null=True)
    ymin = models.FloatField(db_column='yMin', blank=True, null=True)
    ymax = models.FloatField(db_column='yMax', blank=True, null=True)
    zmin = models.FloatField(db_column='zMin', blank=True, null=True)
    zmax = models.FloatField(db_column='zMax', blank=True, null=True)
    factionid = models.IntegerField(
        db_column='factionID', blank=True, null=True)
    nebula = models.IntegerField(blank=True, null=True)
    radius = models.FloatField(blank=True, null=True)

    class Meta:
        """Metadata Options"""
        managed = False
        db_table = 'mapRegions'


class Mapconstellations(models.Model):
    """Model Class representing Constellations"""
    regionid = models.IntegerField(db_column='regionID', blank=True, null=True)
    constellationid = models.AutoField(
        db_column='constellationID', primary_key=True)
    constellationname = models.CharField(
        db_column='constellationName', blank=True, null=True)
    x = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)
    z = models.FloatField(blank=True, null=True)
    xmin = models.FloatField(db_column='xMin', blank=True, null=True)
    xmax = models.FloatField(db_column='xMax', blank=True, null=True)
    ymin = models.FloatField(db_column='yMin', blank=True, null=True)
    ymax = models.FloatField(db_column='yMax', blank=True, null=True)
    zmin = models.FloatField(db_column='zMin', blank=True, null=True)
    zmax = models.FloatField(db_column='zMax', blank=True, null=True)
    factionid = models.IntegerField(
        db_column='factionID', blank=True, null=True)
    radius = models.FloatField(blank=True, null=True)

    class Meta:
        """Metadata Options"""
        managed = False
        db_table = 'mapConstellations'
