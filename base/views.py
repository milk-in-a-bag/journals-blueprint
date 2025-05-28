from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from . models import *
from accounts.models import *

# Create your views here.

@login_required
def home(request):
    return render(request, 'base/home.html')

@login_required
def users(request):
    all_users = MemberProfile.objects.all()
    context = {'users' : all_users}
    return render(request, 'base/users.html', context)

@login_required
def statements(request):
    all_statements = Statement.objects.all().order_by('-uploaded_at')
    all_committees = Committee.objects.all()

    if request.method == 'POST':
        file = request.FILES.get('file')
        committee_id = request.POST.get('committee')
        file_committee = Committee.objects.get(id=committee_id)

        Statement.objects.create(
            file = file,
            committee = file_committee
        )

        return redirect('statements')

    context = {
        'statements' : all_statements,
        'committees' : all_committees
        }
    return render(request, 'base/statements.html', context)

@login_required
def committees(request):
    all_committees = Committee.objects.all()
    context = {'committees' : all_committees}
    return render(request, 'base/committees.html', context)

@login_required
def committee_detail(request, id):
    committee = get_object_or_404(Committee, id=id)
    statements = committee.statements.all()

    context = {
        'committee': committee,
        'statements': statements,
    }
    return render(request, 'base/committee_detail.html', context)