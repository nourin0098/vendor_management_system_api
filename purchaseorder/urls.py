from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('api/purchase_orders/', views.purchaseorder_list),
    path('api/purchase_orders/<int:purchase_order_id>/', views.purchaseorder_details),
]