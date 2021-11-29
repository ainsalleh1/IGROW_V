from django.http.response import Http404
from django.shortcuts import render, redirect, get_object_or_404
# from LOGIN.models import Person as FarmingPerson
# from LOGIN.models import Feed, Booking, Workshop, Group, Member 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, request
from django import forms
# from .forms import CreateInDiscussion, PersonForm, UserUpdateForm
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from django.db.models.signals import post_save
from django.dispatch import receiver
from cryptography.fernet import Fernet
#from django.views.decorators.csrf import csrf_exempt

from group.models import Group
from member.models import Person

#group
def mainGroup(request):
    try:
        group=Group.objects.all()
        person = Person.objects.filter(UserLevel=request.session['UserLevel'])
        return render(request,'MainGroup.html',{'group':group, 'person':person})
    except Group.DoesNotExist:
        raise Http404('Data does not exist')

def GroupAdmin(request):
    try:
        group=Group.objects.all()
        return render(request,'CreategroupAdmin.html',{'group':group})
    except Group.DoesNotExist:
        raise Http404('Data does not exist')


def group(request):
    if request.method=='POST':
        Name=request.POST.get('Name')
        About=request.POST.get('About')
        Media=request.POST.get('Media')
        Group(Name=Name,About=About,Media=Media).save(),
        messages.success(request,'The new group ' + request.POST['Name'] + " is create succesfully..!")
        return render(request,'group.html')

    else :
        return render(request,'group.html')

def myGroup(request):
    try:
        group = Person.objects.get(Username=request.session['Username'])
        return render(request,'MyGroup.html',{'group':group})
    except Group.DoesNotExist:
       raise Http404('Data does not exist')

def updateGroup(request, pk=None):
    #group = Group.objects.filter(Name=request.session['GName'])
    f = Group.objects.get(pk=pk)
    if request.method=='POST':
       #f = Group.objects.get(Name=request.session['GName'])
       f.Name=request.POST['GName']
       f.About=request.POST['GAbout']
       f.Media=request.POST['GMedia']
       f.save()
       messages.success(request,'Group ' + request.POST['GName'] + " details is updated..!")
       return render(request,'MainGroup.html')
    else:
        return render(request, 'homepage.html', {'group':group})