from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

from .forms import RegistrationForm

# Credit where credit's due:
# Views adapted from github:DrkSephy/django-hackathon-starter/

@csrf_protect
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('todo:lists'))
            else:
                return HttpResponse("User Account is not activated")
        else:
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'login.html', {})

@csrf_protect
def register(request):
    if request.method == 'POST':
        user_form = RegistrationForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect(reverse('login'))
        else:
            print(user_form.errors)
    else:
        user_form = RegistrationForm()
    return render(request, 'register.html', {'user_form': user_form} )


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
