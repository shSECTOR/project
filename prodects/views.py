from rest_framework.response import Response
from rest_framework import status,permissions
from rest_framework.views import APIView
from .serializers import ProductSerializer,CategorySerializer
from .models import Product,Category
from django.shortcuts import get_object_or_404


class ProductView(APIView):
    permissions_classes = [permissions.IsAuthenticated]
    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailView(APIView):
    permissions_classes = [permissions.IsAuthenticated]
    def get(self,  id):
        product = get_object_or_404(Product, id=id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, id):
        product = get_object_or_404(Product, id=id)
        serializer = ProductSerializer(data=request.data, instance=product)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        product = get_object_or_404(Product, id=id)
        serializer = ProductSerializer(data=request.data, instance=product, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        product = get_object_or_404(Product, id=id)
        product.delete()
        return Response(
            {'message': "Product deleted"},
            status=status.HTTP_204_NO_CONTENT
        )
    
class CategoriyView(APIView):
    permissions_classes = [permissions.IsAuthenticated]
    def get(self, request, *args, **kwargs):
        categoriys = Category   .objects.all()
        serializer = CategorySerializer(categoriys, many=True)
        return Response(serializer.data)

    
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoriyDetailView(APIView):
    permissions_classes = [permissions.IsAuthenticated]
    def get(self,  id):
        categoriys = get_object_or_404(Category, id=id)
        serializer =  CategorySerializer(categoriys)
        return Response(serializer.data)

    def put(self, request, id):
        categoriys = get_object_or_404(Category, id=id)
        serializer =  CategorySerializer(data=request.data, instance=categoriys)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        categoriys = get_object_or_404(Category, id=id)
        serializer =  CategorySerializer(data=request.data, instance=categoriys, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
