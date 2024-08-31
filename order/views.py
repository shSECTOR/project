from rest_framework.response import Response
from rest_framework import status,permissions
from rest_framework.views import APIView
from .serializers import OrderSerializer
from .models import Order
from django.shortcuts import get_object_or_404


class OrderView(APIView):
    permissions_classes = [permissions.IsAuthenticated]
    def get(self, request, *args, **kwargs):
        order = Order.objects.all()
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderDetailView(APIView):
    permissions_classes = [permissions.IsAuthenticated]
    def get(self, request , id):
        order = get_object_or_404(Order, id=id)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def put(self, request, id):
        order = get_object_or_404(Order, id=id)
        serializer = OrderSerializer(data=request.data, instance=order)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        order = get_object_or_404(Order, id=id)
        serializer = OrderSerializer(data=request.data, instance=order, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        order = get_object_or_404(Order, id=id)
        order.delete()
        return Response(
            {'message': "Order deleted"},
            status=status.HTTP_204_NO_CONTENT
        )
