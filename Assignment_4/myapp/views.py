from django.shortcuts import render
from myapp.models import Restaurant, Recipe, Manu
from django.shortcuts import redirect, get_object_or_404
# Create your views here.
from django.shortcuts import render

def app(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'index.html')

def operation(request):
    res = Restaurant.objects.all()
    context = {
        'res' : res,
    }
    return render(request, 'operations.html', context)

def ADD(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        res = Restaurant(
            name = name,
            email = email,
            address = address,
            phone = phone
        )
        res.save()

    return redirect('operation')

def EDIT(request):
    res = Restaurant.objects.all()
    context = {
        'res' : res,
    }
    
    return redirect(request, 'operations.html', context)

def UPDATE(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        res = Restaurant(
            id = id,
            name = name,
            email = email,
            address = address,
            phone = phone
        )
        res.save()
    return redirect('operation')

def DELETE(request, id):
    res = Restaurant.objects.filter(id = id)
    res.delete()

    context = {
        'res' : res,
    }

    return redirect('operation')

