""" Models for the Buyback App"""
from django.db import models
from eveuniverse.models import EveType


# Create your models here.
class ItemPrices(models.Model):
    """Class representing Item Prices"""
    eve_type = models.OneToOneField(
        EveType,
        on_delete=models.deletion.CASCADE,
        unique=True,
    )
    buy = models.BigIntegerField()
    sell = models.BigIntegerField()
    updated = models.DateTimeField()


class Contract(models.Model):
    """Class representing a Contract"""
    acceptor_id = models.IntegerField()
    assignee_id = models.IntegerField()
    availability = models.CharField(max_length=20)
    contract_id = models.IntegerField(unique=True)
    collateral = models.IntegerField(null=True)
    date_accepted = models.DateTimeField(null=True)
    date_completed = models.DateTimeField(null=True)
    date_expired = models.DateTimeField(null=True)
    date_issued = models.DateTimeField()
    days_to_complete = models.IntegerField()
    end_location_id = models.IntegerField()
    for_corporation = models.BooleanField()
    issuer_corporation_id = models.IntegerField()
    issuer_id = models.IntegerField()
    start_location_id = models.BigIntegerField(null=True)
    location_name = models.CharField(max_length=128, null=True)
    price = models.BigIntegerField()
    reward = models.BigIntegerField()
    status = models.CharField(max_length=30)
    title = models.CharField(max_length=128)
    type = models.CharField(max_length=20)
    volume = models.BigIntegerField()

    def __str__(self) -> str:
        return str(self.contract_id)


class ContractItem(models.Model):
    """Class representing an Item from a Contract"""
    contract = models.ForeignKey(
        Contract,
        on_delete=models.deletion.CASCADE,
        help_text="What contract do these items belong to",
    )
    
    eve_type = models.ForeignKey(
        EveType,
        on_delete=models.deletion.CASCADE,
        help_text="Item type information",
    )

    quantity = models.IntegerField()
