from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.title

class Product(models.Model):
    categoryId = models.ForeignKey(Category, on_delete=models.PROTECT)
    title = models.CharField(max_length=200)
    sell_price = models.DecimalField(max_digits=10, decimal_places=2)
    full_price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product-images/')
    rating = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.title
