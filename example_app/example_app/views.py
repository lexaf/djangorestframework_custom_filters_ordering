# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django.core.exceptions import PermissionDenied
from django.http import Http404
from rest_framework import generics
from rest_framework.exceptions import ParseError
from . import filters

from . import models
from . import serializers


class BookList(generics.ListAPIView):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer
    filter_backend = (filters.RelatedOrderingFilter)
    related_flds = ['shop']


class ShopList(generics.ListAPIView):
    queryset = models.Shop.objects.all()
    serializer_class = serializers.ShopSerializer
    filter_backend = (filters.RelatedOrderingFilter)
    related_flds = ['city']
