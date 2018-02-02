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

        context = {
            'clients': clients,
        }

        return render(request, self.template_name, context)


class AddClient(LoginRequiredMixin, View):
    template_name = 'clients.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


    def post(self, request, *args, **kwargs):
        data = request.POST
        name = data['name']
        contact_person = data['contact_person']
        contact_number = data['contact_number']
        projects = data['projects']

        models.Client.objects.create(
            name = client_name,
            contact_person = contact_person,
            contact_number = contact_number,
            projects = projects
        )

        return redirect(reverse('clients'))

class Projects(LoginRequiredMixin, View):
    template_name = 'projects.html'

    def get(self, request, *args, **kwargs):
        projects = models.Project.objects.all()

        context = {
            'projects': projects,
        }

        return render(request, self.template_name, context)
