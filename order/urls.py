from django.urls import path
from .views import OrderView,OrderDetailView

urlpatterns = [
    path('order/', OrderView.as_view(), name='order-list-create'),  
    path('order/<int:id>/', OrderDetailView.as_view(), name='order-detail'), 
]