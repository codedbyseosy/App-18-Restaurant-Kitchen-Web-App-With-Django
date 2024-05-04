from typing import Any
from django.shortcuts import render
from django.views import generic
from .models import Item, MEAL_TYPE


class MenuList(generic.ListView):
    queryset = Item.objects.order_by("-date_created")
    template_name = "index.html"

    # This is a pre-defined method that we are over-writing
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context["meals"] = MEAL_TYPE
        return context


class About(generic.TemplateView):
    model = Item
    template_name = "about.html"


class MenuItemDetail(generic.DetailView):
    model = Item
    template_name = "menu_item_detail.html"