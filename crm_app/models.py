# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=60)
    contact_person = models.CharField(max_length=60)
    contact_number = models.CharField(max_length=60)


class Project(models.Model):
    ACTIVE = 1
    INACTIVE = 2
    COMPLETE = 3
    PROJECT_STATUSES = (
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive'),
        (COMPLETE, 'Complete'),
    )
    name = models.CharField(max_length=60)
    status = models.PositiveSmallIntegerField(choices = PROJECT_STATUSES)
    assigned_to = models.ForeignKey(Client, on_delete = models.CASCADE)

    def __str__(self):
        return self.name

    def __iter__(self):
        return [ self.name,
                 self.status,
                 self.assigned_to ] 
