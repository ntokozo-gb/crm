from django.conf.urls import url
from django.contrib.auth import views as auth_views
from crm_app import views
from crm_app import forms
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage

urlpatterns = [
    url(r'^\Z', auth_views.LoginView.as_view(
            template_name='login.html',
            form_class=forms.LoginForm
        ), name='signup'),

    url(r'^clients/$', views.Clients.as_view(), name="clients"),
    url(r'^add_client/$', views.AddClient.as_view(), name="add_client"),
    url(r'^edit_client/$', views.EditClient.as_view(), name="edit_client"),

    url(r'^projects/$', views.project_list, name='project_list'),
    url(r'^projects/create/$', views.project_create, name='project_create'),
    url(r'^projects/(?P<pk>\d+)/update/$', views.project_update, name='project_update'),
    url(r'^projects/(?P<pk>\d+)/delete/$', views.project_delete, name='project_delete'),

    url(r'^favicon.ico$',
        RedirectView.as_view(
            url = staticfiles_storage.url('assets/img/favicon.ico'),
        ),
        name = "favicon"
    ),
]
