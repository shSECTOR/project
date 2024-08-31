from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework_simplejwt.tokens import RefreshToken
class User(AbstractUser):

    
    phone_number = models.CharField(max_length=15)
    image = models.ImageField()
    
    
    def __str__(self):
        return self.username
    
    def chek_hash_password(self):
        if not self.password.startswith('pbkdf2_sha256'):
            self.set_password(self.password)    

    def token(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
    
    def save(self, *args, **kwargs):
        self.chek_hash_password()
        super(User, self).save(*args, **kwargs)
    