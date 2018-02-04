# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Django
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string

# Local
from .models import Project, Client
from .forms import ProjectForm


class Clients(LoginRequiredMixin, View):
    template_name = 'clients.html'

    def get(self, request, *args, **kwargs):
        clients = Client.objects.all()

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

        Client.objects.create(
            name = name,
            contact_person = contact_person,
            contact_number = contact_number,
        )

        return redirect(reverse('clients'))


class EditClient(LoginRequiredMixin, View):
    pass


# class Projects(LoginRequiredMixin, View):
#     template_name = 'projects.html'

#     def get(self, request, *args, **kwargs):
#         projects = Project.objects.all()
#         clients = Client.objects.all()

#         context = {
#             'projects': projects,
#             'clients': clients,
#         }
#         return render(request, self.template_name, context)


class AddProject(LoginRequiredMixin, View):
    template_name = 'projects.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


    def post(self, request, *args, **kwargs):
        data = request.POST
        project_name = data['name']
        project_status = data['status']
        client_id = data['assigned_to']
        assigned_client = Client.objects.filter(id=client_id).first()

        project = Project(
            name = project_name,
            status = project_status,
            assigned_to = assigned_client
        )
        project.save()

        return redirect(reverse('projects'))


class EditProject(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        data = request.GET
        project = Project.objects.filter(id=data['id'])
        project_serialized = serializers.serialize('json', project)

        return JsonResponse(project_serialized, safe = False)


def project_list(request):
    template_name = 'projects/project_list.html'
    projects = Project.objects.all()
    context = { 'projects': projects }

    return render(request, template_name, context)


def project_create(request):
    data = dict()

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            projects = Project.objects.all()
            template_name = 'projects/includes/partial_project_list.html'
            data['html_project_list'] = render_to_string(template_name, {'projects': projects})
        else:
            data['form_id_valid'] = False
    else:
        form = ProjectForm()
    
    context = { 'form': form }
    template = 'projects/includes/partial_project_create.html'
    data['html_form'] = render_to_string(template, context, request=request,)

    return JsonResponse(data)