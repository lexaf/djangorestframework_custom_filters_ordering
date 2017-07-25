# -*- coding: utf-8 -*-
from __future__ import absolute_import

import unittest

from django.test import TestCase
from django.test.client import Client

from . import models


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

    def test_book_list(self):
        # All Books sorted by Shop name
        data = self._get_book_list(ordering='city__name')
        for d in data:
            print(d)
        self.assertEqual(data[0]['shop'][0]['city']['name'], "london")
        self.assertEqual(data[0]['shop'][1]['city']['name'], "berlin")
        self.assertEqual(data[1]['shop'][0]['city']['name'], "london")
        self.assertEqual(data[1]['shop'][1]['city']['name'], "berlin")

        print("----")

        data = self._get_book_list(ordering='-city__name')
        for d in data:
            print(d)
        # import pudb; pudb.set_trace()

        self.assertEqual(data[0]['shop'][0]['city']['name'], "london")
        self.assertEqual(data[0]['shop'][1]['city']['name'], "berlin")
        self.assertEqual(data[1]['shop'][0]['city']['name'], "london")
        self.assertEqual(data[1]['shop'][1]['city']['name'], "berlin")

    def test_shop_list(self):
        # All Shops sorted by City name
        data = self._get_shop_list(ordering='-city__name')
        self.assertEqual(data[0]['city'], 1)
        self.assertEqual(data[1]['city'], 2)

        data = self._get_shop_list(ordering='city__name')
        self.assertEqual(data[0]['city'], 2)
        self.assertEqual(data[1]['city'], 1)
