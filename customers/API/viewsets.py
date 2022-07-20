from rest_framework.viewsets import ModelViewSet
from customers.models import Customer
from .serializers import CustomerSerializer
from rest_framework import filters


class CustomerViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Customer.objects.all()    #.order_by('-date_joined')
    serializer_class = CustomerSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    #filterset_fields = ['name',]
    def get_queryset(self):
        return Customer.objects.filter(disable=False)