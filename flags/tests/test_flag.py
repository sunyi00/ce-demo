# -*- coding: utf-8

from django.test import TestCase
from ..models import Flag


class FlagTests(TestCase):

    def test_flag_smoke(self):
        color = Flag.create('color', 'red', 'not green')
        assert color.name == 'color'
        assert color.status == 'red'
        assert color.memo == 'not green'
