# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django.db import models


class Author(models.Model):

    name = models.CharField(max_length=128)


class City(models.Model):

    name = models.CharField(max_length=128)


class Shop(models.Model):

    name = models.CharField(max_length=128)
    city = models.ForeignKey(City)


class Book(models.Model):

    title = models.CharField(max_length=128)
    shop = models.ManyToManyField(Shop)
    author = models.ForeignKey(Author)
