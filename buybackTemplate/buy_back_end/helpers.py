"""Helper functions for Buyback backend"""
from typing import Dict, Union
#import pprint
from sde.models import Invmarketgroups


def dict_dicts() -> Dict[str, Union[str, int, None]]:
    """
    Caller function to create a dictionary
    of dictionaries forming the hierarchy 
    of Market Groups for Eve Online
    """
    market_groups = Invmarketgroups.objects.all()
    market_hierarchy = {}
    for group in market_groups:
        if not group.parentgroupid:
            market_hierarchy[group.marketgroupname] = group.marketgroupid
    recurse_dicts(market_groups, market_hierarchy)
    #pprint.PrettyPrinter(indent=4,sort_dicts=True).pprint(market_hierarchy)
    return market_hierarchy

def recurse_dicts(market_groups, mark_dict) -> Dict[str, Union[str, int, None]]:
    """
    Recursive funciton to work through the layers
    of the Market Group hierarchy from 
    Eve Online and build the dictionaries
    """
    if len(mark_dict) > 1:
        for k, v in mark_dict.items():
            return_dict = {}

            for group in market_groups:
                if group.parentgroupid == v:
                    return_dict[group.marketgroupname] = group.marketgroupid
            recurse_dicts(market_groups, return_dict)
            mark_dict[k] = return_dict

            
    return mark_dict
