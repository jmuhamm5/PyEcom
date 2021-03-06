from decimal import Decimal
from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save, m2m_changed

# Create your models here.

from products.models import Product

User = settings.AUTH_USER_MODEL

class CartManager(models.Manager):
    def new_or_get(self, request):
        cart_id = request.session.get("cart_id", None)
        qs = self.get_queryset().filter(id=cart_id)
        if qs.count() == 1:
            new_obj = False
            cart_obj = qs.first()
            if request.user.is_authenticated and cart_obj.user is None:
                cart_obj.user = request.user
                cart_obj.save()
        else:
            cart_obj = Cart.objects.new(user=request.user)
            new_obj = True
            request.session['cart_id'] = cart_obj.id
        return cart_obj, new_obj

    def new(self, user=None):
        user_obj = None
        if user is not None:
            if user.is_authenticated:
                user_obj = user
        return self.model.objects.create(user=user_obj)

class Cart(models.Model):
    user        = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    products    = models.ManyToManyField(Product, blank=True)
    total       = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    subtotal    = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    #tax         = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    objects = CartManager()

    def __str__(self): # Python 3
        return str(self.id)
    
    def __unicode__(self): # Python 2
        return str(self.id)

    @property
    def name(self):
        return self.title

def m2m_changed_cart_receiver(sender, instance, action, *args, **kwargs):
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        products = instance.products.all()  
        #subtotal = 0
        total = 0
        #tax = 0
        for x in products:
            #subtotal += x.price
            total += x.price            #comment out line
            #tax = subtotal * 0.10
        #if instance.total != subtotal:
        #   instance.total = subtotal + tax
        #   instance.save()
        if instance.subtotal != total:  #comment out block
            instance.subtotal = total
            instance.save()
   

m2m_changed.connect(m2m_changed_cart_receiver, sender=Cart.products.through)

def pre_save_cart_receiver(sender, instance, *args, **kwargs):
    if instance.subtotal > 0:
        #instance.total = instance.subtotal + instance.tax
        #instance.total = instance.subtotal + 10
        instance.total = Decimal(instance.subtotal) * Decimal(1.10) # 10% tax
    else:
        instance.total = 0.00

pre_save.connect(pre_save_cart_receiver, sender=Cart)
    