from rest_framework.viewsets import ModelViewSet
from products.models import Product
from .serializers import ProductSerializer

class ProductViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Product.objects.all()    #.order_by('-date_joined')
    serializer_class = ProductSerializer