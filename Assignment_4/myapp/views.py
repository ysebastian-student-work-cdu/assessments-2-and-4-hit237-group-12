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



def recipe(request):
    re = Recipe.objects.all()
    context = {
        're' : re,
    }
    return render(request, 'recipe.html', context)

def ADD_recipe(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        ingredients = request.POST.get('ingredients')
        instructions = request.POST.get('instructions')

        re = Recipe(
            name = name,
            description = description,
            ingredients = ingredients,
            instructions = instructions
        )
        re.save()

    return redirect('recipe')

def EDIT_recipe(request):
    re = Recipe.objects.all()
    context = {
        're' : re,
    }
    
    return redirect(request, 'recipe.html', context)

def UPDATE_recipe(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        ingredients = request.POST.get('ingredients')
        instructions = request.POST.get('instructions')

        re = Recipe(
            id = id,
            name = name,
            description = description,
            ingredients = ingredients,
            instructions = instructions
        )
        re.save()
    return redirect('recipe')

def DELETE_recipe(request, id):
    re = Recipe.objects.filter(id = id)
    re.delete()

    context = {
        're' : re,
    }

    return redirect('recipe')


def manu(request):
    ma = Manu.objects.all()
    context = {
        'ma' : ma,
    }
    return render(request, 'manu.html', context)

def ADD_manu(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        ingredients = request.POST.get('ingredients')
        restaurant = request.POST.get('restaurant')

        ma = Manu(
            name = name,
            description = description,
            ingredients = ingredients,
            restaurant = restaurant
        )
        ma.save()

    return redirect('manu')



def EDIT_manu(request):
    ma = Manu.objects.all()
    context = {
        'ma' : ma,
    }
    
    return redirect(request, 'manu.html', context)

def UPDATE_manu(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        ingredients = request.POST.get('ingredients')
        restaurant = request.POST.get('restaurant')

        ma = Manu(
            id = id,
            name = name,
            description = description,
            ingredients = ingredients,
            restaurant = restaurant
        )
        ma.save()
    return redirect('manu')

def DELETE_manu(request, id):
    ma = get_object_or_404(Manu, id=id)
    ma.items.clear() 
    ma.delete()

    return redirect('manu')