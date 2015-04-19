# -*- coding: utf-8

from django.test import TestCase
from ..models import Food


class FoodTests(TestCase):

    def test_food_smoke(self):
        rice = Food.create('rice')
        assert rice.name == 'rice'
