# Django
from django import forms
from django.contrib.auth.forms import AuthenticationForm

# Crispy forms
from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Submit, HTML, Div, Field
from crispy_forms.bootstrap import FormActions


class LoginForm(AuthenticationForm):
    helper = FormHelper()
    helper.form_class = "form-login"
    helper.form_show_labels = False
    helper.layout = Layout(
        HTML('<h2 class="form-login-heading">login</h2>'),
        Div(
            Field(
                'username',
                placeholder="Username"
            ),
            Field(
                'password',
                placeholder="Password"
            ),
            FormActions(
                Submit(
                    'login',
                    'Sign in',
                    css_class='btn btn-theme btn-block'
                )
            ),
            css_class='login-wrap'
        ),
    )
