from django.shortcuts import render
from django.urls import reverse_lazy
from . import forms
from django.views.generic import CreateView

# Create your views here.


class SignUp(CreateView):
    form_class = forms.UserCreateForm  # 4
    success_url = reverse_lazy("login")  # 5
    template_name = "accounts/signup.html"
