from django.shortcuts import render
from myapp.models import Restaurant, Recipe, Manu
from django.shortcuts import redirect, get_object_or_404
# Create your views here.
from django.shortcuts import render

def app(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'index.html')
