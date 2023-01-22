
from django.urls import path
from .views import HomeView, ItemDetailView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('detail/<slug>/', ItemDetailView.as_view(), name="detail")
]
