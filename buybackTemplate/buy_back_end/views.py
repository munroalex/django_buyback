"""View functions for the Buy Back back end funcitonality"""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from buy_back_end.helpers import dict_dicts #build_tree
from sde.models import Invtypes, Invmarketgroups
import pprint

# Create your views here.

@login_required
def edit_bb_items(request):
    """Display all item types in side menu with Buyback editable options"""
    hierarchy = dict_dicts()
    pprint.PrettyPrinter(indent=4,sort_dicts=True).pprint(hierarchy)
    #print(hierarchy)
    return render(request, 'items.html', {'hierarchy':hierarchy})
