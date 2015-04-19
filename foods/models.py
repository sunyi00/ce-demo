# -*- coding: utf-8

from django.db import models


class Food(models.Model):

    name = models.CharField(max_length=100, default="food")

    @classmethod
    def create(cls, name):
        f = Food()
        f.name = name
        f.save()
        return f

    def __unicode__(self):
        return "<%s:%s>" % (self.id, self.name, )
