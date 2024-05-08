from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import PurchaseOrder
from .serializers import PurchaseOrderSerializer

@api_view(['GET', 'POST'])
def purchaseorder_list(request):
    if request.method == 'GET':
        purchaseorder = PurchaseOrder.objects.all()
        serializer = PurchaseOrderSerializer(purchaseorder, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PurchaseOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def purchaseorder_details(request, purchase_order_id):
    try:
        purchaseorder = PurchaseOrder.objects.get(pk=purchase_order_id)
    except PurchaseOrder.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PurchaseOrderSerializer(purchaseorder)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PurchaseOrderSerializer(purchaseorder, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        purchaseorder.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


