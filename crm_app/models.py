# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Client(models.Model):
    client_name = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=100)


class Project(models.Model):
    clients = models.ManyToManyField(Client)
    proj_name = models.CharField(max_length=100)
    status = models.CharField(max_length=15)
