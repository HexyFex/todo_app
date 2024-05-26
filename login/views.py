from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Login


# Create your views here.
class TaskList(ListView):
    model = Login
