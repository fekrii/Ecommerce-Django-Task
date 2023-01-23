
from django.urls import path
from .views import HomeView, ItemDetailView, add_to_cart, OrderSummaryView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('detail/<slug>/', ItemDetailView.as_view(), name="detail"),
    path('add-to-cart/<slug>/', add_to_cart, name='add_to_cart'),
    path('order-summary/', OrderSummaryView.as_view(), name='order_summary'),
]
