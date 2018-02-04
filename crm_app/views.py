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
from .forms import ProjectForm, ClientForm


def client_update(request):
  pass


def client_delete(request):
  pass


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


def project_list(request):
  template_name = 'projects/project_list.html'
  projects = Project.objects.all()
  context = { 'projects': projects }

  return render(request, template_name, context)


def project_create(request):
  if request.method == 'POST':
    form = ProjectForm(request.POST)
  else:
    form = ProjectForm()

  template = 'projects/includes/partial_project_create.html'
  return save_project_form(request, form, template)


def project_update(request, pk):
  project = get_object_or_404(Project, pk=pk)
  if request.method == 'POST':
    form = ProjectForm(request.POST, instance=project)
  else:
    form = ProjectForm(instance=project)
  
  template = 'projects/includes/partial_project_update.html'
  return save_project_form(request, form, template)


def save_project_form(request, form, template_name):
  data = dict()
  if request.method == 'POST':
    form = ProjectForm(request.POST)
    if form.is_valid():
      form.save()
      form.objects.filter
      data['form_is_valid'] = True
      projects = Project.objects.all()
      template_name = 'projects/includes/partial_project_list.html'
      data['html_project_list'] = render_to_string(
          template_name, 
          { 'projects': projects }
      )
    else:
      data['form_id_valid'] = False

  context = { 'form': form }
  data['html_form'] = render_to_string(template_name, context, request=request)

  return JsonResponse(data)


def project_delete(request, pk):
  data = dict()
  project = get_object_or_404(Project, pk=pk)

  if request.method == 'POST':
    project.delete()
    data['form_is_valid'] = True
    projects = Project.objects.all()
    template = 'projects/includes/partial_project_list.html'
    data['html_project_list'] = render_to_string(template, {'projects': projects})
  else:
    context = {'project': project}
    template_delete = 'projects/includes/partial_project_delete.html'
    data['html_form'] = render_to_string(template_delete, context, request=request)
  
  return JsonResponse(data)


def client_list(request):
  template_name = 'clients/client_list.html'
  clients = Client.objects.all()
  context = { 'clients': clients }

  return render(request, template_name, context)


def client_create(request):
  if request.method == 'POST':
    form = ClientForm(request.POST)
  else:
    form = ClientForm()

  template = 'clients/includes/partial_client_create.html'
  return save_client_form(request, form, template)


def save_client_form(request, form, template_name):
  data = dict()
  if request.method == 'POST':
    form = ClientForm(request.POST)
    if form.is_valid():
      form.save()
      form.objects.filter
      data['form_is_valid'] = True
      clients = Client.objects.all()
      template_name = 'projects/includes/partial_project_list.html'
      data['html_project_list'] = render_to_string(
          template_name, 
          { 'clients': clients }
      )
    else:
      data['form_id_valid'] = False

  context = { 'form': form }
  data['html_form'] = render_to_string(template_name, context, request=request)

  return JsonResponse(data)
