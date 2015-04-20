# -*- coding: utf-8

from django.test import TestCase
from django.test import Client
import json

from foods.models import Food


class FoodListTests(TestCase):

        def test_food_list_smoke(self):
            Food.create('meat')
            c = Client()
            response = c.get('/foods')
            assert response.status_code == 200
            assert json.loads(response.content)


class FoodDetailTests(TestCase):

        def test_food_detail_smoke(self):
            Food.create('rice')
            c1 = Client()
            response = c1.get('/foods/1/')
            assert response.status_code == 200
            assert json.loads(response.content)
