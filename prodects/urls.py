from django.urls import path
from .views import ProductView, ProductDetailView,CategoriyDetailView,CategoriyView

urlpatterns = [
    path('products/', ProductView.as_view(), name='product-list-create'),  
    path('products/<int:id>/', ProductDetailView.as_view(), name='product-detail'),  
    path('categorys/', CategoriyView.as_view(), name='categorys-list-create'),  
    path('categorys /<int:id>/', CategoriyDetailView.as_view(), name='categorys-detail'),  
    ]
# +998950192366