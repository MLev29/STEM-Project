# Create your views here.
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader

def index(request):
    return render(request, "catalog/home.html")