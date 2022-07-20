from django.contrib.auth.models import User
from django.db import models
from customers.models import Customer
from products.models import Product

# Create your models here.


class Payment(models.Model):
    payments = models.CharField(max_length=15)

    def __str__(self):
        return self.payments


class Order(models.Model):
    seller = models.ForeignKey(User,null=True, on_delete=models.SET_NULL)
    customer = models.ForeignKey(Customer,null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product,null=True, on_delete=models.SET_NULL)
    date = models.DateTimeField(auto_now_add=True)
    units = models.IntegerField(default=1, verbose_name='Unit(s)')
    payment = models.ForeignKey(Payment, null=True, on_delete=models.SET_NULL)



    def __str__(self):
        return self.seller.username

