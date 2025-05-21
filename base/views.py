from django.shortcuts import render
from . models import *

# Create your views here.

def home(request):
    return render(request, 'base/home.html')

def users(request):
    return render(request, 'base/users.html')

def statements(request):
    statements = Statement.objects.all()
    context = {'statements' : statements}
    return render(request, 'base/statements.html', context)