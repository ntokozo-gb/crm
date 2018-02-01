from django.conf.urls import url
from django.contrib.auth import views as auth_views
from crm_app import views
from crm_app import forms

urlpatterns = [
    url(r'^\Z', auth_views.LoginView.as_view(
            template_name='login.html',
            form_class=forms.LoginForm
        ), name='signup'),
    url(r'^clients/$', views.Clients.as_view(), name="clients"),
    url(r'^add_client/$', views.AddClient.as_view(), name="add_client"),
]
