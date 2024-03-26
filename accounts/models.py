from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager
# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    """
    Creating our User Model 

    """
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=11, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    fullname= models.CharField(max_length=100)
    
    objects = UserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email', 'fullname']

    def __str__(self):
        return self.email

    
    @property
    def is_staff(self):
        return self.is_admin
    

class OptCode(models.Model):
    phone = models.CharField(max_length=11, unique=True)
    code = models.PositiveSmallIntegerField()
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.phone} created at {self.created} by this code {self.code}'
