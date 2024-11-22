from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView
from .models import User
class UserListView(ListView):
    model = User
    template_name = "user_list.html"
    context_object_name = "users"

 