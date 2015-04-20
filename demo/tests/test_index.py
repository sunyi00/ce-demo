# -*- coding: utf-8

from django.test import TestCase
from django.test import Client
from flags.models import Flag


class IndexTests(TestCase):

    def test_index_smoke(self):
        c = Client()
        response = c.get('/')
        assert response.status_code == 200
        assert response.content == 'white'

    def test_index_red(self):
        try:
            red = Flag.objects.get(name='color')
        except Flag.DoesNotExist:
            red = Flag.create('color', 'red', 'not green')
        c = Client()
        response = c.get('/')
        assert response.status_code == 200
        assert response.content == red.status
