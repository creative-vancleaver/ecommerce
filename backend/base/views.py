import json
# from msilib.schema import ReserveCost
from django.shortcuts import render

from django.http import JsonResponse

from  .models import Product
from .serializers import ProductSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .products import products

# Create your views here.

@api_view(['GET'])
def getRoutes(request):

    routes = [

        '/api/products',
        '/api/products/create/',

        '/api/products/upload/',

        '/api/prouducts/<id>/reviews/',

        '/api/products/top/',
        '/api/products/<id>/',

        '/api/products/delete/<id>/',
        '/api/products/<update>/<id>/', 

    ]

    # return JsonResponse(routes, safe=False)
    return Response(routes)


def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def getProduct(request, pk):

    product = None

    for i in products:
        if i['_id'] == pk:
            product = i
            break

    return Response(product)
