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

        models.Client.objects.create(
            name = name,
            contact_person = contact_person,
            contact_number = contact_number,
        )

        return redirect(reverse('clients'))


class Projects(LoginRequiredMixin, View):
    template_name = 'projects.html'

    def get(self, request, *args, **kwargs):
        projects = models.Project.objects.all()
        clients = models.Client.objects.all()

        context = {
            'projects': projects,
            'clients': clients,
        }
        return render(request, self.template_name, context)


class AddProject(LoginRequiredMixin, View):
    template_name = 'projects.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


    def post(self, request, *args, **kwargs):
        data = request.POST
        project_name = data['name']
        project_status = data['status']
        assigned_to = data['assigned_to']

        models.Project.objects.create(
            name = project_name,
            status = project_status,
            assigned_to = assigned_to
        )

        return redirect(reverse('projects'))
