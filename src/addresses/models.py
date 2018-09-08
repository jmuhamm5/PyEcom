from django.db import models

from billing.models import BillingProfile

ADDRESS_TYPES = (
    ('billing', 'Billing'),
    ('shipping', 'Shipping')
)

# Create your models here.

class Address(models.Model):
    billing_profile     = models.ForeignKey(BillingProfile, null=False, blank=False, on_delete=models.CASCADE)
    address_type        = models.CharField(max_length=120, choices=ADDRESS_TYPES)
    address_line_1      = models.CharField(max_length=120)
    address_line_2      = models.CharField(max_length=120, null=True, blank=True)
    city                = models.CharField(max_length=120)
    state               = models.CharField(max_length=120)
    country             = models.CharField(max_length=120, default='United States')
    postal_code         = models.CharField(max_length=120)

    def __str__(self): #python3
        return str(self.billing_profile)
    
    def __unicode__(self): #python2
        return str(self.billing_profile)
    