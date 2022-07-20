"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from rest_framework import routers
from customers.API.viewsets import CustomerViewSet
from products.API.viewsets import ProductViewSet
from orders.API.viewsets import OrderViewSet, OrderList, TotalAmount


router = routers.DefaultRouter()
router.register(r'customers', CustomerViewSet, basename='Customer')
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('customer_orders/<str:customer_cpf>', OrderList.as_view()),
    path('total_amount/', TotalAmount.as_view()),
    path('admin/', admin.site.urls),
]
