# -*- coding: utf-8 -*-
from __future__ import absolute_import

import unittest

from django.test import TestCase
from django.test.client import Client

from .models import Book


class OrderingTestCase(TestCase):

    fixtures = ['test.json']

    def setUp(self):
        self.client = Client()

    def _get_shop_list(self, token=None, **params):
        resp = self.client.get('/shop',
                               {key: val for key, val in params.items() if val is not None})
        self.assertEqual(resp.status_code, 200, resp.content)
        return resp.data

    def _get_book_list(self, token=None, **params):
        resp = self.client.get('/book',
                               {key: val for key, val in params.items() if val is not None})
        self.assertEqual(resp.status_code, 200, resp.content)
        return resp.data

    def test_sort_book_by_author(self):
        # Books sorted by Author name
        data = self._get_book_list(ordering='-author__name')
        self.assertEqual(
            data[0]['author']['name'],
            Book.objects.all().order_by('-author__name').first().author.name
        )
        self.assertEqual(
            data[-1]['author']['name'],
            Book.objects.all().order_by('-author__name').last().author.name
        )

        data = self._get_book_list(ordering='author__name')
        self.assertEqual(
            data[0]['author']['name'],
            Book.objects.all().order_by('author__name').first().author.name
        )
        self.assertEqual(
            data[-1]['author']['name'],
            Book.objects.all().order_by('author__name').last().author.name
        )

    @unittest.skip('ManyToMany relation does not work')
    def test_sort_book_by_shop_name(self):
        # Books sorted by Shop name
        data = self._get_book_list(ordering='-shop__name')
        book = Book.objects.first()
        self.assertEqual(data[0]['shop'][0]['name'], book.shop.first().name)
        self.assertEqual(data[0]['shop'][1]['name'], book.shop.last().name)
        data = self._get_book_list(ordering='shop__name')
        self.assertEqual(data[0]['shop'][0]['name'], book.shop.last().name)
        self.assertEqual(data[0]['shop'][1]['name'], book.shop.first().name)

    def test_sort_shop_by_city_name(self):
        # Shops sorted by City name
        data = self._get_shop_list(ordering='-city__name')
        self.assertEqual(data[0]['city']['name'], 'stockolm')
        self.assertEqual(data[1]['city']['name'], 'london')
        self.assertEqual(data[2]['city']['name'], 'berlin')

        data = self._get_shop_list(ordering='city__name')
        self.assertEqual(data[0]['city']['name'], 'berlin')
        self.assertEqual(data[1]['city']['name'], 'london')
        self.assertEqual(data[2]['city']['name'], 'stockolm')
