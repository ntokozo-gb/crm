# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=60)
    status = models.CharField(max_length=15)


class Client(models.Model):
    name = models.CharField(max_length=60)
    contact_person = models.CharField(max_length=60)
    contact_number = models.CharField(max_length=60)
    projects = models.ManyToManyField(Project)
