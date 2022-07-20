from dataclasses import field
from itertools import product
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from orders.models import Order

from customers.API.serializers import CustomerSerializer
from products.API.serializers import ProductSerializer



class OrderSerializer(ModelSerializer):
    customer = CustomerSerializer()
    product = ProductSerializer()
    seller = SerializerMethodField()
    date = SerializerMethodField()
    total = SerializerMethodField()

    class Meta:
        model = Order
        fields = ('id', 'seller', 'customer', 'product', 'date','units','payment', 'total')
        depth = 1

    def get_seller(self, obj):
        return obj.seller.username

    def get_date(self, obj):
        return obj.date.strftime("%m/%d/%Y")

    def get_total(self, obj):
        return obj.product.price
