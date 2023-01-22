from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from .models import *
class HomeView(View):
    def get(self, *args, **kwargs):
        items = Item.objects.all()
        context = {
            "items":items
        }
        return render(self.request, 'index.html', context)

class ItemDetailView(DetailView):
    model = Item
    template_name = "item.html"