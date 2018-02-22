# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=60)
    contact_person = models.CharField(max_length=60)
    contact_number = models.CharField(max_length=60)
    objects = models.Manager() # to get rid of pylint warnings

    def __str__(self):
      return self.name

    def __iter__(self):
      return iter(self.name, self.contact_person, self.contact_number)


class Project(models.Model):
    ACTIVE = 0
    INACTIVE = 1
    COMPLETE = 2
    PROJECT_STATUSES = (
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive'),
        (COMPLETE, 'Complete'),
    )
    name = models.CharField(max_length=60)
    project_status = models.PositiveSmallIntegerField(choices = PROJECT_STATUSES)
    assigned_to = models.ForeignKey(Client, on_delete = models.CASCADE)
    objects = models.Manager() # to get rid of pylint warnings

    def __str__(self):
      return self.name

    def __iter__(self):
      return iter(self.name, self.project_status, self.assigned_to) 
