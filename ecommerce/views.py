from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.views.generic import ListView, DetailView, View
from django.contrib import messages
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from notifications.models import OrderNotification
from datetime import datetime
class HomeView(View):
    def get(self, *args, **kwargs):
        items = Item.objects.all()
        context = {
            "items":items,
            "room_name": "orderComplete"
        }
        return render(self.request, 'index.html', context)


class ItemDetailView(LoginRequiredMixin, DetailView):
    model = Item
    template_name = "item.html"



def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False,
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.success(request, f"{item}'s quantity was updated")
            return redirect('order_summary')
        else:
            order.items.add(order_item)
            messages.success(request, f"{item} was added to your cart")
            OrderNotification.objects.create(message="order adde to cart", time=datetime.now(), sent=True)
            return redirect('order_summary')
    else:
        # ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user, ordered=False)  # ordered_date=ordered_date)
        order.items.add(order_item)
        messages.success(request, f"{item} was added to your cart")
        OrderNotification.objects.create(message="order adde to cart", time=datetime.now(), sent=True)
        return redirect('order_summary')


class OrderSummaryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'orders': order,
                'user':self.request.user
            }

            return render(self.request, 'cart.html', context)
        except ObjectDoesNotExist:
            messages.info(self.request, "You don't have an active order!")
            return redirect('home')