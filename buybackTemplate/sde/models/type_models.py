"""Module for all SDE models relating directly to item types."""
from django.db import models

# Create your models here.

class Invcategories(models.Model):
    """Model Class representing Item Type Categories"""
    categoryid = models.AutoField(db_column='categoryID', primary_key=True)
    categoryname = models.CharField(db_column='categoryName', )
    iconid = models.IntegerField(db_column='iconID', null=True)
    published = models.BooleanField(null=True)

    class Meta:
        """Metadata Options"""
        managed = False
        db_table = 'invCategories'


class Invgroups(models.Model):
    """Model Class representing Inventory Item Groups"""
    groupid = models.AutoField(db_column='groupID', primary_key=True)
    categoryid = models.IntegerField(db_column='categoryID', null=True)
    groupname = models.CharField(db_column='groupName')
    iconid = models.IntegerField(db_column='iconID', null=True)
    usebaseprice = models.BooleanField(db_column='useBasePrice', null=True)
    anchored = models.BooleanField(null=True)
    anchorable = models.BooleanField(null=True)
    fittablenonsingleton = models.BooleanField(
        db_column='fittableNonSingleton', null=True)
    published = models.BooleanField(null=True)

    class Meta:
        """Metadata Options"""
        managed = False
        db_table = 'invGroups'


class Invitems(models.Model):
    """Model Class representing Inventory Items"""
    itemid = models.AutoField(db_column='itemID', primary_key=True)
    typeid = models.IntegerField(db_column='typeID')
    ownerid = models.IntegerField(db_column='ownerID')
    locationid = models.IntegerField(db_column='locationID')
    flagid = models.IntegerField(db_column='flagID')
    quantity = models.IntegerField()

    class Meta:
        """Metadata Options"""
        managed = False
        db_table = 'invItems'


class Invmarketgroups(models.Model):
    """Model Class representing Inventory Item Market Groups"""
    marketgroupid = models.AutoField(
        db_column='marketGroupID', primary_key=True)
    parentgroupid = models.IntegerField(db_column='parentGroupID', null=True)
    marketgroupname = models.CharField(db_column='marketGroupName')
    description = models.CharField(null=True)
    iconid = models.IntegerField(db_column='iconID', null=True)
    hastypes = models.BooleanField(db_column='hasTypes', null=True)

    class Meta:
        """Metadata Options"""
        managed = False
        db_table = 'invMarketGroups'


class Invmetagroups(models.Model):
    """Model Class representing Inventory Item Meta Groups"""
    metagroupid = models.AutoField(db_column='metaGroupID', primary_key=True)
    metagroupname = models.CharField(db_column='metaGroupName')
    description = models.CharField(null=True)
    iconid = models.IntegerField(db_column='iconID', null=True)

    class Meta:
        """Metadata Options"""
        managed = False
        db_table = 'invMetaGroups'


class Invmetatypes(models.Model):
    """Model Class representing Inventory Item Meta Groups"""
    typeid = models.AutoField(db_column='typeID', primary_key=True)
    parenttypeid = models.IntegerField(db_column='parentTypeID', null=True)
    metagroupid = models.IntegerField(db_column='metaGroupID', null=True)

    class Meta:
        """Metadata Options"""
        managed = False
        db_table = 'invMetaTypes'


class Invnames(models.Model):
    """Model Class representing Inventory Item Names"""
    itemid = models.AutoField(db_column='itemID', primary_key=True)
    itemname = models.CharField(db_column='itemName')

    class Meta:
        """Metadata Options"""
        managed = False
        db_table = 'invNames'


class Invtypematerials(models.Model):
    """Model Class representing Inventory Item Traits"""
    typeid = models.AutoField(db_column='typeID', primary_key=True)
    materialtypeid = models.IntegerField(db_column='materialTypeID')
    quantity = models.IntegerField()

    class Meta:
        """Metadata Options"""
        managed = False
        db_table = 'invTypeMaterials'
        unique_together = ['typeid', 'materialtypeid']


class Invtypereactions(models.Model):
    """Model Class representing Inventory Item Reactions"""
    reactiontypeid = models.AutoField(
        db_column='reactionTypeID', primary_key=True)
    input = models.BooleanField()
    typeid = models.IntegerField(db_column='typeID')
    quantity = models.IntegerField(null=True)

    class Meta:
        """Metadata Options"""
        managed = False
        db_table = 'invTypeReactions'
        unique_together = ['reactiontypeid', 'input', 'typeid']


class Invtypes(models.Model):
    """Model Class representing Inventory Item Types"""
    typeid = models.AutoField(db_column='typeID', primary_key=True)
    groupid = models.IntegerField(db_column='groupID', null=True)
    typename = models.CharField(db_column='typeName', null=True)
    description = models.TextField(null=True)
    mass = models.FloatField(null=True)
    volume = models.FloatField(null=True)
    capacity = models.FloatField(null=True)
    portionsize = models.IntegerField(db_column='portionSize', null=True)
    raceid = models.IntegerField(db_column='raceID', null=True)
    baseprice = models.FloatField(db_column='basePrice', null=True)
    published = models.BooleanField(null=True)
    marketgroupid = models.IntegerField(db_column='marketGroupID', null=True)
    iconid = models.IntegerField(db_column='iconID', null=True)
    soundid = models.IntegerField(db_column='soundID', null=True)
    graphicid = models.IntegerField(db_column='graphicID', null=True)

    class Meta:
        """Metadata Options"""
        managed = False
        db_table = 'invTypes'
