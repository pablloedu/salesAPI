from rest_framework.serializers import ModelSerializer
from customers.models import Customer


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        #fields = ('id','name', 'addres', 'birth_date','cpf','phone_number', 'disable')
        fields = '__all__'
