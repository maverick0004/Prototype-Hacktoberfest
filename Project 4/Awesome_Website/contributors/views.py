from django.shortcuts import render, redirect
from django.http import HttpResponse,Http404
from .models import Contributor
from .forms import ContributorForm

def add(request):
    if request.method == 'POST':
        form = ContributorForm(request.POST)
        if form.is_valid():
            #Contributor.objects.create()
            new  = form.save()
            print('hello')
            return HttpResponse('You\'ve been added to Contributors')
    
    else:
        form = ContributorForm()
        args = {'form' : form}
        return render(request,'landing.html',args)