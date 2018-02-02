# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Django
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

# Local
from . import models


class Clients(LoginRequiredMixin, View):
    template_name = 'clients.html'

    def get(self, request, *args, **kwargs):
        clients = models.Client.objects.all()
        projects = models.Project.objects.all()

        context = {
            'clients': clients,
            'projects': projects,
        }

        return render(request, self.template_name, context)


class AddClient(LoginRequiredMixin, View):
    template_name = 'clients.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


    def post(self, request, *args, **kwargs):
        data = request.POST
        client_name = data['client_name']
        contact_person = data['contact_person']
        contact_number = data['contact_number']
        models.Client.objects.create(
            client_name=client_name,
            contact_person=contact_person,
            contact_number=contact_number
        )

        return redirect(reverse('clients'))
