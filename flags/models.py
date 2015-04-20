# -*- coding: utf-8

from django.db import models


class Flag(models.Model):

    name = models.CharField(max_length=100, default="flag")
    status = models.CharField(max_length=100, default="")
    memo = models.TextField(default='')

    @classmethod
    def create(cls, name, status, memo):
        f = Flag()
        f.name = name
        f.status = status
        f.memo = memo
        f.save()
        return f

    def __unicode__(self):
        return "<%s:%s:%s>" % (self.id, self.name, self.status )
