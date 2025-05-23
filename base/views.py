from django.shortcuts import render, get_object_or_404
from . models import *

# Create your views here.

def home(request):
    return render(request, 'base/home.html')

def users(request):
    return render(request, 'base/users.html')

def statements(request):
    all_statements = Statement.objects.all()
    all_committees = Committee.objects.all()

    context = {'statements' : all_statements,
               'committees' : all_committees}
    return render(request, 'base/statements.html', context)

def committees(request):
    all_committees = Committee.objects.all()
    context = {'committees' : all_committees}
    return render(request, 'base/committees.html', context)

def committee_detail(request, id):
    committee = get_object_or_404(Committee, id=id)
    statements = committee.statements.all()
    context = {
        'committee': committee,
        'statements': statements,
    }
    return render(request, 'base/committee_detail.html', context)