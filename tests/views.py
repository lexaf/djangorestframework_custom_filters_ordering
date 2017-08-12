# -*- coding: utf-8 -*-
from __future__ import absolute_import

from rest_framework import generics
from . import filters
from . import models
from . import serializers


class BookList(generics.ListAPIView):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer
    filter_backend = (filters.RelatedOrderingFilter,)
    related_flds = ['shop']
    ordering_fields = '__all__'


class ShopList(generics.ListAPIView):
    queryset = models.Shop.objects.all()
    serializer_class = serializers.ShopSerializer
    filter_backend = (filters.RelatedOrderingFilter,)
    related_flds = ['city']
    ordering_fields = '__all__'
