from itertools import product
from django.urls import path
from . import views
from .models import Product
urlpatterns = [
    path('',views.products_list),
    path('<int:pk>/', views.products_list),
    
]