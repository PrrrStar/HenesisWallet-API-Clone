'''
from django.shortcuts import render


from rest_framework.views import APIView

from .serializers import CommentSerializer
from .serializers import ProductSerializer
from .serializers import CategorySerializer

from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import (generics, authentication, permissions, filters,)


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):

        return Response({
            'products-category': reverse(ProductCategoryList.name, request=request),
            'products-best': reverse(ProductBestList.name, request=request),
            'products-list': reverse(ProductList.name, request=request),
            'isLoggedIn': isLoggedIn,
        })

class ProductCategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name','description',]
    name = 'products-category'

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name','description',]
    name = 'products-list'
'''