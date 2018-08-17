from django.conf import settings
from django.db import models

# Create your models here.

from products.models import Product

User = settings.AUTH_USER_MODEL

class Cart(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    product     = models.ManyToManyField(Product, blank=True)
    total       = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    updated     = models.DateTimeField(auto_now_add=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self): # Python 3
        return self.id
    
    def __unicode__(self): # Python 2
        return self.id

