from django.db import models
from users.models import User
from prodects.models import Product
from django.utils import timezone

class Order(models.Model):
    ORDER_STATUS = (
        ('PENDING', 'PENDING'),
        ('PROSESS', 'PROSESS'),
        ('DASTAVCHIK', 'DASTAVCHIK'),
        ('DELEVIERED', 'DELEVIERED'),
        ('CANCELED', 'CANCELED')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='order')
    qty = models.IntegerField()
    price = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=255, choices=ORDER_STATUS, default='PENDING')
    def str(self) -> str:
        return self.qty
    
    
    def total_price(self):
        return self.qty * self.price