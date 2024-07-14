# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Agtagenttypes(models.Model):
    agenttypeid = models.AutoField(db_column='agentTypeID', primary_key=True)  # Field name made lowercase.
    agenttype = models.CharField(db_column='agentType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'agtAgentTypes'


class Agtagents(models.Model):
    agentid = models.AutoField(db_column='agentID', primary_key=True)  # Field name made lowercase.
    divisionid = models.IntegerField(db_column='divisionID', blank=True, null=True)  # Field name made lowercase.
    corporationid = models.IntegerField(db_column='corporationID', blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='locationID', blank=True, null=True)  # Field name made lowercase.
    level = models.IntegerField(blank=True, null=True)
    quality = models.IntegerField(blank=True, null=True)
    agenttypeid = models.IntegerField(db_column='agentTypeID', blank=True, null=True)  # Field name made lowercase.
    islocator = models.BooleanField(db_column='isLocator', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'agtAgents'


class Agtagentsinspace(models.Model):
    agentid = models.AutoField(db_column='agentID', primary_key=True)  # Field name made lowercase.
    dungeonid = models.IntegerField(db_column='dungeonID', blank=True, null=True)  # Field name made lowercase.
    solarsystemid = models.IntegerField(db_column='solarSystemID', blank=True, null=True)  # Field name made lowercase.
    spawnpointid = models.IntegerField(db_column='spawnPointID', blank=True, null=True)  # Field name made lowercase.
    typeid = models.IntegerField(db_column='typeID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'agtAgentsInSpace'


class Agtresearchagents(models.Model):
    agentid = models.AutoField(db_column='agentID', primary_key=True)  # Field name made lowercase. The composite primary key (agentID, typeID) found, that is not supported. The first column is selected.
    typeid = models.IntegerField(db_column='typeID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'agtResearchAgents'


class Certcerts(models.Model):
    certid = models.AutoField(db_column='certID', primary_key=True)  # Field name made lowercase.
    description = models.TextField(blank=True, null=True)
    groupid = models.IntegerField(db_column='groupID', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'certCerts'


class Certmasteries(models.Model):
    typeid = models.IntegerField(db_column='typeID', blank=True, null=True)  # Field name made lowercase.
    masterylevel = models.IntegerField(db_column='masteryLevel', blank=True, null=True)  # Field name made lowercase.
    certid = models.IntegerField(db_column='certID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'certMasteries'


class Certskills(models.Model):
    certid = models.IntegerField(db_column='certID', blank=True, null=True)  # Field name made lowercase.
    skillid = models.IntegerField(db_column='skillID', blank=True, null=True)  # Field name made lowercase.
    certlevelint = models.IntegerField(db_column='certLevelInt', blank=True, null=True)  # Field name made lowercase.
    skilllevel = models.IntegerField(db_column='skillLevel', blank=True, null=True)  # Field name made lowercase.
    certleveltext = models.CharField(db_column='certLevelText', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'certSkills'


class Chrancestries(models.Model):
    ancestryid = models.AutoField(db_column='ancestryID', primary_key=True)  # Field name made lowercase.
    ancestryname = models.CharField(db_column='ancestryName', blank=True, null=True)  # Field name made lowercase.
    bloodlineid = models.IntegerField(db_column='bloodlineID', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(blank=True, null=True)
    perception = models.IntegerField(blank=True, null=True)
    willpower = models.IntegerField(blank=True, null=True)
    charisma = models.IntegerField(blank=True, null=True)
    memory = models.IntegerField(blank=True, null=True)
    intelligence = models.IntegerField(blank=True, null=True)
    iconid = models.IntegerField(db_column='iconID', blank=True, null=True)  # Field name made lowercase.
    shortdescription = models.CharField(db_column='shortDescription', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'chrAncestries'


class Chrattributes(models.Model):
    attributeid = models.AutoField(db_column='attributeID', primary_key=True)  # Field name made lowercase.
    attributename = models.CharField(db_column='attributeName', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(blank=True, null=True)
    iconid = models.IntegerField(db_column='iconID', blank=True, null=True)  # Field name made lowercase.
    shortdescription = models.CharField(db_column='shortDescription', blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chrAttributes'


class Chrbloodlines(models.Model):
    bloodlineid = models.AutoField(db_column='bloodlineID', primary_key=True)  # Field name made lowercase.
    bloodlinename = models.CharField(db_column='bloodlineName', blank=True, null=True)  # Field name made lowercase.
    raceid = models.IntegerField(db_column='raceID', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(blank=True, null=True)
    maledescription = models.CharField(db_column='maleDescription', blank=True, null=True)  # Field name made lowercase.
    femaledescription = models.CharField(db_column='femaleDescription', blank=True, null=True)  # Field name made lowercase.
    shiptypeid = models.IntegerField(db_column='shipTypeID', blank=True, null=True)  # Field name made lowercase.
    corporationid = models.IntegerField(db_column='corporationID', blank=True, null=True)  # Field name made lowercase.
    perception = models.IntegerField(blank=True, null=True)
    willpower = models.IntegerField(blank=True, null=True)
    charisma = models.IntegerField(blank=True, null=True)
    memory = models.IntegerField(blank=True, null=True)
    intelligence = models.IntegerField(blank=True, null=True)
    iconid = models.IntegerField(db_column='iconID', blank=True, null=True)  # Field name made lowercase.
    shortdescription = models.CharField(db_column='shortDescription', blank=True, null=True)  # Field name made lowercase.
    shortmaledescription = models.CharField(db_column='shortMaleDescription', blank=True, null=True)  # Field name made lowercase.
    shortfemaledescription = models.CharField(db_column='shortFemaleDescription', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'chrBloodlines'


class Chrfactions(models.Model):
    factionid = models.AutoField(db_column='factionID', primary_key=True)  # Field name made lowercase.
    factionname = models.CharField(db_column='factionName', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(blank=True, null=True)
    raceids = models.IntegerField(db_column='raceIDs', blank=True, null=True)  # Field name made lowercase.
    solarsystemid = models.IntegerField(db_column='solarSystemID', blank=True, null=True)  # Field name made lowercase.
    corporationid = models.IntegerField(db_column='corporationID', blank=True, null=True)  # Field name made lowercase.
    sizefactor = models.TextField(db_column='sizeFactor', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    stationcount = models.IntegerField(db_column='stationCount', blank=True, null=True)  # Field name made lowercase.
    stationsystemcount = models.IntegerField(db_column='stationSystemCount', blank=True, null=True)  # Field name made lowercase.
    militiacorporationid = models.IntegerField(db_column='militiaCorporationID', blank=True, null=True)  # Field name made lowercase.
    iconid = models.IntegerField(db_column='iconID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'chrFactions'


class Chrraces(models.Model):
    raceid = models.AutoField(db_column='raceID', primary_key=True)  # Field name made lowercase.
    racename = models.CharField(db_column='raceName', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(blank=True, null=True)
    iconid = models.IntegerField(db_column='iconID', blank=True, null=True)  # Field name made lowercase.
    shortdescription = models.CharField(db_column='shortDescription', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'chrRaces'


class Crpactivities(models.Model):
    activityid = models.AutoField(db_column='activityID', primary_key=True)  # Field name made lowercase.
    activityname = models.CharField(db_column='activityName', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crpActivities'


class Crpnpccorporationdivisions(models.Model):
    corporationid = models.AutoField(db_column='corporationID', primary_key=True)  # Field name made lowercase. The composite primary key (corporationID, divisionID) found, that is not supported. The first column is selected.
    divisionid = models.IntegerField(db_column='divisionID')  # Field name made lowercase.
    size = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crpNPCCorporationDivisions'


class Crpnpccorporationresearchfields(models.Model):
    skillid = models.AutoField(db_column='skillID', primary_key=True)  # Field name made lowercase. The composite primary key (skillID, corporationID) found, that is not supported. The first column is selected.
    corporationid = models.IntegerField(db_column='corporationID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'crpNPCCorporationResearchFields'


class Crpnpccorporationtrades(models.Model):
    corporationid = models.AutoField(db_column='corporationID', primary_key=True)  # Field name made lowercase. The composite primary key (corporationID, typeID) found, that is not supported. The first column is selected.
    typeid = models.IntegerField(db_column='typeID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'crpNPCCorporationTrades'


class Crpnpccorporations(models.Model):
    corporationid = models.AutoField(db_column='corporationID', primary_key=True)  # Field name made lowercase.
    size = models.CharField(blank=True, null=True)
    extent = models.CharField(blank=True, null=True)
    solarsystemid = models.IntegerField(db_column='solarSystemID', blank=True, null=True)  # Field name made lowercase.
    investorid1 = models.IntegerField(db_column='investorID1', blank=True, null=True)  # Field name made lowercase.
    investorshares1 = models.IntegerField(db_column='investorShares1', blank=True, null=True)  # Field name made lowercase.
    investorid2 = models.IntegerField(db_column='investorID2', blank=True, null=True)  # Field name made lowercase.
    investorshares2 = models.IntegerField(db_column='investorShares2', blank=True, null=True)  # Field name made lowercase.
    investorid3 = models.IntegerField(db_column='investorID3', blank=True, null=True)  # Field name made lowercase.
    investorshares3 = models.IntegerField(db_column='investorShares3', blank=True, null=True)  # Field name made lowercase.
    investorid4 = models.IntegerField(db_column='investorID4', blank=True, null=True)  # Field name made lowercase.
    investorshares4 = models.IntegerField(db_column='investorShares4', blank=True, null=True)  # Field name made lowercase.
    friendid = models.IntegerField(db_column='friendID', blank=True, null=True)  # Field name made lowercase.
    enemyid = models.IntegerField(db_column='enemyID', blank=True, null=True)  # Field name made lowercase.
    publicshares = models.IntegerField(db_column='publicShares', blank=True, null=True)  # Field name made lowercase.
    initialprice = models.IntegerField(db_column='initialPrice', blank=True, null=True)  # Field name made lowercase.
    minsecurity = models.TextField(db_column='minSecurity', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    scattered = models.BooleanField(blank=True, null=True)
    fringe = models.IntegerField(blank=True, null=True)
    corridor = models.IntegerField(blank=True, null=True)
    hub = models.IntegerField(blank=True, null=True)
    border = models.IntegerField(blank=True, null=True)
    factionid = models.IntegerField(db_column='factionID', blank=True, null=True)  # Field name made lowercase.
    sizefactor = models.TextField(db_column='sizeFactor', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    stationcount = models.IntegerField(db_column='stationCount', blank=True, null=True)  # Field name made lowercase.
    stationsystemcount = models.IntegerField(db_column='stationSystemCount', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(blank=True, null=True)
    iconid = models.IntegerField(db_column='iconID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'crpNPCCorporations'


class Crpnpcdivisions(models.Model):
    divisionid = models.AutoField(db_column='divisionID', primary_key=True)  # Field name made lowercase.
    divisionname = models.CharField(db_column='divisionName', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(blank=True, null=True)
    leadertype = models.CharField(db_column='leaderType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'crpNPCDivisions'


class Dgmattributecategories(models.Model):
    categoryid = models.AutoField(db_column='categoryID', primary_key=True)  # Field name made lowercase.
    categoryname = models.CharField(db_column='categoryName', blank=True, null=True)  # Field name made lowercase.
    categorydescription = models.CharField(db_column='categoryDescription', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dgmAttributeCategories'


class Dgmattributetypes(models.Model):
    attributeid = models.AutoField(db_column='attributeID', primary_key=True)  # Field name made lowercase.
    attributename = models.CharField(db_column='attributeName', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(blank=True, null=True)
    iconid = models.IntegerField(db_column='iconID', blank=True, null=True)  # Field name made lowercase.
    defaultvalue = models.TextField(db_column='defaultValue', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    published = models.BooleanField(blank=True, null=True)
    displayname = models.CharField(db_column='displayName', blank=True, null=True)  # Field name made lowercase.
    unitid = models.IntegerField(db_column='unitID', blank=True, null=True)  # Field name made lowercase.
    stackable = models.BooleanField(blank=True, null=True)
    highisgood = models.BooleanField(db_column='highIsGood', blank=True, null=True)  # Field name made lowercase.
    categoryid = models.IntegerField(db_column='categoryID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dgmAttributeTypes'


class Dgmeffects(models.Model):
    effectid = models.AutoField(db_column='effectID', primary_key=True)  # Field name made lowercase.
    effectname = models.CharField(db_column='effectName', blank=True, null=True)  # Field name made lowercase.
    effectcategory = models.IntegerField(db_column='effectCategory', blank=True, null=True)  # Field name made lowercase.
    preexpression = models.IntegerField(db_column='preExpression', blank=True, null=True)  # Field name made lowercase.
    postexpression = models.IntegerField(db_column='postExpression', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(blank=True, null=True)
    guid = models.CharField(blank=True, null=True)
    iconid = models.IntegerField(db_column='iconID', blank=True, null=True)  # Field name made lowercase.
    isoffensive = models.BooleanField(db_column='isOffensive', blank=True, null=True)  # Field name made lowercase.
    isassistance = models.BooleanField(db_column='isAssistance', blank=True, null=True)  # Field name made lowercase.
    durationattributeid = models.IntegerField(db_column='durationAttributeID', blank=True, null=True)  # Field name made lowercase.
    trackingspeedattributeid = models.IntegerField(db_column='trackingSpeedAttributeID', blank=True, null=True)  # Field name made lowercase.
    dischargeattributeid = models.IntegerField(db_column='dischargeAttributeID', blank=True, null=True)  # Field name made lowercase.
    rangeattributeid = models.IntegerField(db_column='rangeAttributeID', blank=True, null=True)  # Field name made lowercase.
    falloffattributeid = models.IntegerField(db_column='falloffAttributeID', blank=True, null=True)  # Field name made lowercase.
    disallowautorepeat = models.BooleanField(db_column='disallowAutoRepeat', blank=True, null=True)  # Field name made lowercase.
    published = models.BooleanField(blank=True, null=True)
    displayname = models.CharField(db_column='displayName', blank=True, null=True)  # Field name made lowercase.
    iswarpsafe = models.BooleanField(db_column='isWarpSafe', blank=True, null=True)  # Field name made lowercase.
    rangechance = models.BooleanField(db_column='rangeChance', blank=True, null=True)  # Field name made lowercase.
    electronicchance = models.BooleanField(db_column='electronicChance', blank=True, null=True)  # Field name made lowercase.
    propulsionchance = models.BooleanField(db_column='propulsionChance', blank=True, null=True)  # Field name made lowercase.
    distribution = models.IntegerField(blank=True, null=True)
    sfxname = models.CharField(db_column='sfxName', blank=True, null=True)  # Field name made lowercase.
    npcusagechanceattributeid = models.IntegerField(db_column='npcUsageChanceAttributeID', blank=True, null=True)  # Field name made lowercase.
    npcactivationchanceattributeid = models.IntegerField(db_column='npcActivationChanceAttributeID', blank=True, null=True)  # Field name made lowercase.
    fittingusagechanceattributeid = models.IntegerField(db_column='fittingUsageChanceAttributeID', blank=True, null=True)  # Field name made lowercase.
    modifierinfo = models.TextField(db_column='modifierInfo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dgmEffects'


class Dgmexpressions(models.Model):
    expressionid = models.AutoField(db_column='expressionID', primary_key=True)  # Field name made lowercase.
    operandid = models.IntegerField(db_column='operandID', blank=True, null=True)  # Field name made lowercase.
    arg1 = models.IntegerField(blank=True, null=True)
    arg2 = models.IntegerField(blank=True, null=True)
    expressionvalue = models.CharField(db_column='expressionValue', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(blank=True, null=True)
    expressionname = models.CharField(db_column='expressionName', blank=True, null=True)  # Field name made lowercase.
    expressiontypeid = models.IntegerField(db_column='expressionTypeID', blank=True, null=True)  # Field name made lowercase.
    expressiongroupid = models.IntegerField(db_column='expressionGroupID', blank=True, null=True)  # Field name made lowercase.
    expressionattributeid = models.IntegerField(db_column='expressionAttributeID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dgmExpressions'


class Dgmtypeattributes(models.Model):
    typeid = models.AutoField(db_column='typeID', primary_key=True)  # Field name made lowercase. The composite primary key (typeID, attributeID) found, that is not supported. The first column is selected.
    attributeid = models.IntegerField(db_column='attributeID')  # Field name made lowercase.
    valueint = models.IntegerField(db_column='valueInt', blank=True, null=True)  # Field name made lowercase.
    valuefloat = models.TextField(db_column='valueFloat', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'dgmTypeAttributes'


class Dgmtypeeffects(models.Model):
    typeid = models.AutoField(db_column='typeID', primary_key=True)  # Field name made lowercase. The composite primary key (typeID, effectID) found, that is not supported. The first column is selected.
    effectid = models.IntegerField(db_column='effectID')  # Field name made lowercase.
    isdefault = models.BooleanField(db_column='isDefault', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dgmTypeEffects'


class Evegraphics(models.Model):
    graphicid = models.AutoField(db_column='graphicID', primary_key=True)  # Field name made lowercase.
    soffactionname = models.CharField(db_column='sofFactionName', blank=True, null=True)  # Field name made lowercase.
    graphicfile = models.CharField(db_column='graphicFile', blank=True, null=True)  # Field name made lowercase.
    sofhullname = models.CharField(db_column='sofHullName', blank=True, null=True)  # Field name made lowercase.
    sofracename = models.CharField(db_column='sofRaceName', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eveGraphics'


class Eveicons(models.Model):
    iconid = models.AutoField(db_column='iconID', primary_key=True)  # Field name made lowercase.
    iconfile = models.CharField(db_column='iconFile', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eveIcons'


class Eveunits(models.Model):
    unitid = models.AutoField(db_column='unitID', primary_key=True)  # Field name made lowercase.
    unitname = models.CharField(db_column='unitName', blank=True, null=True)  # Field name made lowercase.
    displayname = models.CharField(db_column='displayName', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eveUnits'






















class Mapcelestialgraphics(models.Model):
    celestialid = models.AutoField(db_column='celestialID', primary_key=True)  # Field name made lowercase.
    heightmap1 = models.IntegerField(db_column='heightMap1', blank=True, null=True)  # Field name made lowercase.
    heightmap2 = models.IntegerField(db_column='heightMap2', blank=True, null=True)  # Field name made lowercase.
    shaderpreset = models.IntegerField(db_column='shaderPreset', blank=True, null=True)  # Field name made lowercase.
    population = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mapCelestialGraphics'


class Mapcelestialstatistics(models.Model):
    celestialid = models.AutoField(db_column='celestialID', primary_key=True)  # Field name made lowercase.
    temperature = models.TextField(blank=True, null=True)  # This field type is a guess.
    spectralclass = models.CharField(db_column='spectralClass', blank=True, null=True)  # Field name made lowercase.
    luminosity = models.TextField(blank=True, null=True)  # This field type is a guess.
    age = models.TextField(blank=True, null=True)  # This field type is a guess.
    life = models.TextField(blank=True, null=True)  # This field type is a guess.
    orbitradius = models.TextField(db_column='orbitRadius', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    eccentricity = models.TextField(blank=True, null=True)  # This field type is a guess.
    massdust = models.TextField(db_column='massDust', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    massgas = models.TextField(db_column='massGas', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fragmented = models.BooleanField(blank=True, null=True)
    density = models.TextField(blank=True, null=True)  # This field type is a guess.
    surfacegravity = models.TextField(db_column='surfaceGravity', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    escapevelocity = models.TextField(db_column='escapeVelocity', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    orbitperiod = models.TextField(db_column='orbitPeriod', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    rotationrate = models.TextField(db_column='rotationRate', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    locked = models.BooleanField(blank=True, null=True)
    pressure = models.TextField(blank=True, null=True)  # This field type is a guess.
    radius = models.TextField(blank=True, null=True)  # This field type is a guess.
    mass = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mapCelestialStatistics'


class Mapconstellationjumps(models.Model):
    fromregionid = models.IntegerField(db_column='fromRegionID', blank=True, null=True)  # Field name made lowercase.
    fromconstellationid = models.AutoField(db_column='fromConstellationID', primary_key=True)  # Field name made lowercase. The composite primary key (fromConstellationID, toConstellationID) found, that is not supported. The first column is selected.
    toconstellationid = models.IntegerField(db_column='toConstellationID')  # Field name made lowercase.
    toregionid = models.IntegerField(db_column='toRegionID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mapConstellationJumps'



class Mapdenormalize(models.Model):
    itemid = models.AutoField(db_column='itemID', primary_key=True)  # Field name made lowercase.
    typeid = models.IntegerField(db_column='typeID', blank=True, null=True)  # Field name made lowercase.
    groupid = models.IntegerField(db_column='groupID', blank=True, null=True)  # Field name made lowercase.
    solarsystemid = models.IntegerField(db_column='solarSystemID', blank=True, null=True)  # Field name made lowercase.
    constellationid = models.IntegerField(db_column='constellationID', blank=True, null=True)  # Field name made lowercase.
    regionid = models.IntegerField(db_column='regionID', blank=True, null=True)  # Field name made lowercase.
    orbitid = models.IntegerField(db_column='orbitID', blank=True, null=True)  # Field name made lowercase.
    x = models.TextField(blank=True, null=True)  # This field type is a guess.
    y = models.TextField(blank=True, null=True)  # This field type is a guess.
    z = models.TextField(blank=True, null=True)  # This field type is a guess.
    radius = models.TextField(blank=True, null=True)  # This field type is a guess.
    itemname = models.CharField(db_column='itemName', blank=True, null=True)  # Field name made lowercase.
    security = models.TextField(blank=True, null=True)  # This field type is a guess.
    celestialindex = models.IntegerField(db_column='celestialIndex', blank=True, null=True)  # Field name made lowercase.
    orbitindex = models.IntegerField(db_column='orbitIndex', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mapDenormalize'


class Mapjumps(models.Model):
    stargateid = models.AutoField(db_column='stargateID', primary_key=True)  # Field name made lowercase.
    destinationid = models.IntegerField(db_column='destinationID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mapJumps'


class Maplandmarks(models.Model):
    landmarkid = models.AutoField(db_column='landmarkID', primary_key=True)  # Field name made lowercase.
    landmarkname = models.CharField(db_column='landmarkName', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(blank=True, null=True)
    locationid = models.IntegerField(db_column='locationID', blank=True, null=True)  # Field name made lowercase.
    x = models.TextField(blank=True, null=True)  # This field type is a guess.
    y = models.TextField(blank=True, null=True)  # This field type is a guess.
    z = models.TextField(blank=True, null=True)  # This field type is a guess.
    iconid = models.IntegerField(db_column='iconID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mapLandmarks'


class Maplocationscenes(models.Model):
    locationid = models.AutoField(db_column='locationID', primary_key=True)  # Field name made lowercase.
    graphicid = models.IntegerField(db_column='graphicID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mapLocationScenes'


class Maplocationwormholeclasses(models.Model):
    locationid = models.AutoField(db_column='locationID', primary_key=True)  # Field name made lowercase.
    wormholeclassid = models.IntegerField(db_column='wormholeClassID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mapLocationWormholeClasses'


class Mapregionjumps(models.Model):
    fromregionid = models.AutoField(db_column='fromRegionID', primary_key=True)  # Field name made lowercase. The composite primary key (fromRegionID, toRegionID) found, that is not supported. The first column is selected.
    toregionid = models.IntegerField(db_column='toRegionID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mapRegionJumps'








class Mapuniverse(models.Model):
    universeid = models.AutoField(db_column='universeID', primary_key=True)  # Field name made lowercase.
    universename = models.CharField(db_column='universeName', blank=True, null=True)  # Field name made lowercase.
    x = models.TextField(blank=True, null=True)  # This field type is a guess.
    y = models.TextField(blank=True, null=True)  # This field type is a guess.
    z = models.TextField(blank=True, null=True)  # This field type is a guess.
    xmin = models.TextField(db_column='xMin', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    xmax = models.TextField(db_column='xMax', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ymin = models.TextField(db_column='yMin', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ymax = models.TextField(db_column='yMax', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    zmin = models.TextField(db_column='zMin', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    zmax = models.TextField(db_column='zMax', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    radius = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mapUniverse'


class Planetschematics(models.Model):
    schematicid = models.AutoField(db_column='schematicID', primary_key=True)  # Field name made lowercase.
    schematicname = models.CharField(db_column='schematicName', blank=True, null=True)  # Field name made lowercase.
    cycletime = models.IntegerField(db_column='cycleTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'planetSchematics'


class Planetschematicspinmap(models.Model):
    schematicid = models.AutoField(db_column='schematicID', primary_key=True)  # Field name made lowercase. The composite primary key (schematicID, pinTypeID) found, that is not supported. The first column is selected.
    pintypeid = models.IntegerField(db_column='pinTypeID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'planetSchematicsPinMap'


class Planetschematicstypemap(models.Model):
    schematicid = models.AutoField(db_column='schematicID', primary_key=True)  # Field name made lowercase. The composite primary key (schematicID, typeID) found, that is not supported. The first column is selected.
    typeid = models.IntegerField(db_column='typeID')  # Field name made lowercase.
    quantity = models.IntegerField(blank=True, null=True)
    isinput = models.BooleanField(db_column='isInput', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'planetSchematicsTypeMap'


class Ramassemblylinestations(models.Model):
    stationid = models.AutoField(db_column='stationID', primary_key=True)  # Field name made lowercase. The composite primary key (stationID, assemblyLineTypeID) found, that is not supported. The first column is selected.
    assemblylinetypeid = models.IntegerField(db_column='assemblyLineTypeID')  # Field name made lowercase.
    quantity = models.IntegerField(blank=True, null=True)
    stationtypeid = models.IntegerField(db_column='stationTypeID', blank=True, null=True)  # Field name made lowercase.
    ownerid = models.IntegerField(db_column='ownerID', blank=True, null=True)  # Field name made lowercase.
    solarsystemid = models.IntegerField(db_column='solarSystemID', blank=True, null=True)  # Field name made lowercase.
    regionid = models.IntegerField(db_column='regionID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ramAssemblyLineStations'


class Ramassemblylinetypedetailpercategory(models.Model):
    assemblylinetypeid = models.AutoField(db_column='assemblyLineTypeID', primary_key=True)  # Field name made lowercase. The composite primary key (assemblyLineTypeID, categoryID) found, that is not supported. The first column is selected.
    categoryid = models.IntegerField(db_column='categoryID')  # Field name made lowercase.
    timemultiplier = models.TextField(db_column='timeMultiplier', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    materialmultiplier = models.TextField(db_column='materialMultiplier', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    costmultiplier = models.TextField(db_column='costMultiplier', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'ramAssemblyLineTypeDetailPerCategory'


class Ramassemblylinetypedetailpergroup(models.Model):
    assemblylinetypeid = models.AutoField(db_column='assemblyLineTypeID', primary_key=True)  # Field name made lowercase. The composite primary key (assemblyLineTypeID, groupID) found, that is not supported. The first column is selected.
    groupid = models.IntegerField(db_column='groupID')  # Field name made lowercase.
    timemultiplier = models.TextField(db_column='timeMultiplier', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    materialmultiplier = models.TextField(db_column='materialMultiplier', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    costmultiplier = models.TextField(db_column='costMultiplier', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'ramAssemblyLineTypeDetailPerGroup'


class Ramassemblylinetypes(models.Model):
    assemblylinetypeid = models.AutoField(db_column='assemblyLineTypeID', primary_key=True)  # Field name made lowercase.
    assemblylinetypename = models.CharField(db_column='assemblyLineTypeName', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(blank=True, null=True)
    basetimemultiplier = models.TextField(db_column='baseTimeMultiplier', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    basematerialmultiplier = models.TextField(db_column='baseMaterialMultiplier', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    basecostmultiplier = models.TextField(db_column='baseCostMultiplier', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    volume = models.TextField(blank=True, null=True)  # This field type is a guess.
    activityid = models.IntegerField(db_column='activityID', blank=True, null=True)  # Field name made lowercase.
    mincostperhour = models.TextField(db_column='minCostPerHour', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'ramAssemblyLineTypes'


class Raminstallationtypecontents(models.Model):
    installationtypeid = models.AutoField(db_column='installationTypeID', primary_key=True)  # Field name made lowercase. The composite primary key (installationTypeID, assemblyLineTypeID) found, that is not supported. The first column is selected.
    assemblylinetypeid = models.IntegerField(db_column='assemblyLineTypeID')  # Field name made lowercase.
    quantity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ramInstallationTypeContents'


class Skinlicense(models.Model):
    licensetypeid = models.AutoField(db_column='licenseTypeID', primary_key=True)  # Field name made lowercase.
    duration = models.IntegerField(blank=True, null=True)
    skinid = models.IntegerField(db_column='skinID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'skinLicense'


class Skinmaterials(models.Model):
    skinmaterialid = models.AutoField(db_column='skinMaterialID', primary_key=True)  # Field name made lowercase.
    displaynameid = models.IntegerField(db_column='displayNameID', blank=True, null=True)  # Field name made lowercase.
    materialsetid = models.IntegerField(db_column='materialSetID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'skinMaterials'


class Skinship(models.Model):
    skinid = models.IntegerField(db_column='skinID', blank=True, null=True)  # Field name made lowercase.
    typeid = models.IntegerField(db_column='typeID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'skinShip'


class Skins(models.Model):
    skinid = models.AutoField(db_column='skinID', primary_key=True)  # Field name made lowercase.
    internalname = models.CharField(db_column='internalName', blank=True, null=True)  # Field name made lowercase.
    skinmaterialid = models.IntegerField(db_column='skinMaterialID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'skins'


class Staoperationservices(models.Model):
    operationid = models.AutoField(db_column='operationID', primary_key=True)  # Field name made lowercase. The composite primary key (operationID, serviceID) found, that is not supported. The first column is selected.
    serviceid = models.IntegerField(db_column='serviceID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'staOperationServices'


class Staoperations(models.Model):
    activityid = models.IntegerField(db_column='activityID', blank=True, null=True)  # Field name made lowercase.
    operationid = models.AutoField(db_column='operationID', primary_key=True)  # Field name made lowercase.
    operationname = models.CharField(db_column='operationName', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(blank=True, null=True)
    fringe = models.IntegerField(blank=True, null=True)
    corridor = models.IntegerField(blank=True, null=True)
    hub = models.IntegerField(blank=True, null=True)
    border = models.IntegerField(blank=True, null=True)
    ratio = models.IntegerField(blank=True, null=True)
    caldaristationtypeid = models.IntegerField(db_column='caldariStationTypeID', blank=True, null=True)  # Field name made lowercase.
    minmatarstationtypeid = models.IntegerField(db_column='minmatarStationTypeID', blank=True, null=True)  # Field name made lowercase.
    amarrstationtypeid = models.IntegerField(db_column='amarrStationTypeID', blank=True, null=True)  # Field name made lowercase.
    gallentestationtypeid = models.IntegerField(db_column='gallenteStationTypeID', blank=True, null=True)  # Field name made lowercase.
    jovestationtypeid = models.IntegerField(db_column='joveStationTypeID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'staOperations'


class Staservices(models.Model):
    serviceid = models.AutoField(db_column='serviceID', primary_key=True)  # Field name made lowercase.
    servicename = models.CharField(db_column='serviceName', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staServices'


class Stastationtypes(models.Model):
    stationtypeid = models.AutoField(db_column='stationTypeID', primary_key=True)  # Field name made lowercase.
    dockentryx = models.TextField(db_column='dockEntryX', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dockentryy = models.TextField(db_column='dockEntryY', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dockentryz = models.TextField(db_column='dockEntryZ', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dockorientationx = models.TextField(db_column='dockOrientationX', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dockorientationy = models.TextField(db_column='dockOrientationY', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dockorientationz = models.TextField(db_column='dockOrientationZ', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    operationid = models.IntegerField(db_column='operationID', blank=True, null=True)  # Field name made lowercase.
    officeslots = models.IntegerField(db_column='officeSlots', blank=True, null=True)  # Field name made lowercase.
    reprocessingefficiency = models.TextField(db_column='reprocessingEfficiency', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conquerable = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staStationTypes'



class Translationtables(models.Model):
    sourcetable = models.CharField(db_column='sourceTable', primary_key=True)  # Field name made lowercase. The composite primary key (sourceTable, translatedKey) found, that is not supported. The first column is selected.
    destinationtable = models.CharField(db_column='destinationTable', blank=True, null=True)  # Field name made lowercase.
    translatedkey = models.CharField(db_column='translatedKey')  # Field name made lowercase.
    tcgroupid = models.IntegerField(db_column='tcGroupID', blank=True, null=True)  # Field name made lowercase.
    tcid = models.IntegerField(db_column='tcID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'translationTables'


class Trntranslationcolumns(models.Model):
    tcgroupid = models.IntegerField(db_column='tcGroupID', blank=True, null=True)  # Field name made lowercase.
    tcid = models.AutoField(db_column='tcID', primary_key=True)  # Field name made lowercase.
    tablename = models.CharField(db_column='tableName')  # Field name made lowercase.
    columnname = models.CharField(db_column='columnName')  # Field name made lowercase.
    masterid = models.CharField(db_column='masterID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'trnTranslationColumns'


class Trntranslationlanguages(models.Model):
    numericlanguageid = models.AutoField(db_column='numericLanguageID', primary_key=True)  # Field name made lowercase.
    languageid = models.CharField(db_column='languageID', blank=True, null=True)  # Field name made lowercase.
    languagename = models.CharField(db_column='languageName', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'trnTranslationLanguages'


class Trntranslations(models.Model):
    tcid = models.AutoField(db_column='tcID', primary_key=True)  # Field name made lowercase. The composite primary key (tcID, keyID, languageID) found, that is not supported. The first column is selected.
    keyid = models.IntegerField(db_column='keyID')  # Field name made lowercase.
    languageid = models.CharField(db_column='languageID')  # Field name made lowercase.
    text = models.TextField()

    class Meta:
        managed = False
        db_table = 'trnTranslations'


class Warcombatzonesystems(models.Model):
    solarsystemid = models.AutoField(db_column='solarSystemID', primary_key=True)  # Field name made lowercase.
    combatzoneid = models.IntegerField(db_column='combatZoneID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'warCombatZoneSystems'


class Warcombatzones(models.Model):
    combatzoneid = models.AutoField(db_column='combatZoneID', primary_key=True)  # Field name made lowercase.
    combatzonename = models.CharField(db_column='combatZoneName', blank=True, null=True)  # Field name made lowercase.
    factionid = models.IntegerField(db_column='factionID', blank=True, null=True)  # Field name made lowercase.
    centersystemid = models.IntegerField(db_column='centerSystemID', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'warCombatZones'
