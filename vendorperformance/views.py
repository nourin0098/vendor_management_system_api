from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from .models import Vendor, VendorPerformance
from .serializers import VendorPerformanceSerializer

from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from .models import VendorPerformance
from .serializers import VendorPerformanceSerializer

class VendorPerformanceAPIView(generics.RetrieveAPIView):
    serializer_class = VendorPerformanceSerializer
    lookup_url_kwarg = 'vendor_id'

    def get_queryset(self):
        vendor_id = self.kwargs.get('vendor_id')
        return VendorPerformance.objects.filter(vendor_id=vendor_id)

    def retrieve(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset.exists():
            return Response({"message": "Vendor performance data not found."}, status=404)
        
        instance = queryset.latest('date')
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

