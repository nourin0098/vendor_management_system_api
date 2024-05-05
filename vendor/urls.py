from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('api/vendors/', views.vendor_list),
    path('api/vendors/<int:vendor_id>/', views.vendor_detail),
]
