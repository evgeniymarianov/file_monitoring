from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView,CreateView, UpdateView,DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from accounts.models import Document
import json
from django.http import StreamingHttpResponse
from django.views.generic.base import View
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_exempt

def indexView(request):
     return render(request, 'index.html')

@login_required
def dashboardView(request):
    documents = Document.objects.all()
    if request.method == "GET":
        return render(request, 'dashboard.html', {'documents': documents})
    if request.method == "POST":
        uploaded_file = Document(
            description = request.POST['description'],
            document = request.FILES['document']
        )
        uploaded_file.save()
    return render(request, 'dashboard.html', {'documents': documents})

def registerView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form':form})
