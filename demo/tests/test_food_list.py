# -*- coding: utf-8

from django.test import TestCase
from django.test import Client
import json


class FoodListTests(TestCase):

        def test_food_list_smoke(self):
            c = Client()
            response = c.get('/foods')
            assert response.status_code == 200
            assert json.loads(response.content)
