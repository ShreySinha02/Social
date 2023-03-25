from django.shortcuts import render
from django.urls import reverse_lazy
# from django.urls import reverse
# from django.urls import 
from django.views.generic import CreateView
from . import forms
# Create your views here.
class SignUp(CreateView):
    form_class=forms.UserCreateForm  # connection to usercreateform
    success_url=reverse_lazy("login")
    template_name='accounts/signup.html' #which template to use