
from django.urls import path

from . import views

urlpatterns = [
    path("", views.edit_bb_items, name="items"),
]
