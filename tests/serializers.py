# -*- coding: utf-8 -*-
from __future__ import absolute_import

from rest_framework import serializers

from . import models

class AuthorSerializer(serializers.ModelSerializer):

    name = serializers.CharField()

    class Meta:
        model = models.Author
        fields = ['name']


class CitySerializer(serializers.ModelSerializer):

    name = serializers.CharField()

    class Meta:
        model = models.City
        fields = ['name']


class ShopSerializer(serializers.ModelSerializer):

    name = serializers.CharField()
    city = CitySerializer()

    class Meta:
        model = models.Shop
        fields = ['name', 'city']


class BookSerializer(serializers.ModelSerializer):

    title = serializers.CharField()
    author = AuthorSerializer()
    shop = ShopSerializer(many=True)

    class Meta:
        model = models.Book
        fields = ['title', 'shop', 'author']
