from django.shortcuts import render, render_to_response
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/login/")
    else:
        form = UserCreationForm()
    return render_to_response("register.html", {'form': form,})
@csrf_exempt
@login_required
def index(request):
    
    return render_to_response("index.html", {'username': request.user.username})

@csrf_exempt
@login_required
def ensure_logout(request):
    if request.method == 'POST':
        if request.POST.has_key('ensure'):
            auth.logout(request)
            return HttpResponseRedirect("/login/")
        else:
            return HttpResponseRedirect("/index/")
    return render_to_response("logout.html")
