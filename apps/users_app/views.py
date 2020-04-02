from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm

from apps.travel_notes_app import views


def logout_request(request):
    logout(request)
    return HttpResponseRedirect(reverse(views.index))

def register(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        # Processing filled form
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse(views.index))
    context = {'form':form}
    return render(request, 'users/register.html', context)


