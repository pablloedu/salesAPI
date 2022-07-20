from rest_framework.viewsets import ModelViewSet
from orders.models import Order
from .serializers import OrderSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):

        return Order.objects.filter(customer__cpf='06482124321')



class OrderList(generics.ListAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):

        cpf = self.kwargs['customer_cpf']
        return Order.objects.filter(customer__cpf=cpf)

class TotalAmount(APIView):
    def get(self, request):
        valores=[]
        orders = Order.objects.all()
        for order in orders:
            valores.append(order.product.price)
        total_amount = sum(valores)
        return Response({'total_amount':total_amount},status=status.HTTP_200_OK)