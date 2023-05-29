from django.shortcuts import render
from myapp.models import Food_waste_Audit, Food_Items, Waste_Types
from django.shortcuts import redirect, get_object_or_404
# Create your views here.
from django.shortcuts import render

def app(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'index.html')

def Food_waste(request):
    res = Food_waste_Audit.objects.all()
    context = {
        'res' : res,
    }
    return render(request, 'food_waste.html', context)

def ADD(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        res = Food_waste_Audit(
            name = name,
            email = email,
            address = address,
            phone = phone
        )
        res.save()

    return redirect('Food_waste')

def EDIT(request):
    res = Food_waste_Audit.objects.all()
    context = {
        'res' : res,
    }
    
    return redirect(request, 'food_waste.html', context)

def UPDATE(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        res = Food_waste_Audit(
            id = id,
            name = name,
            email = email,
            address = address,
            phone = phone
        )
        res.save()
    return redirect('Food_waste')

def DELETE(request, id):
    res = Food_waste_Audit.objects.filter(id = id)
    res.delete()

    context = {
        'res' : res,
    }

    return redirect('Food_waste')



def food_item(request):
    re = Food_Items.objects.all()
    context = {
        're' : re,
    }
    return render(request, 'food_item.html', context)

def ADD_food_item(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        ingredients = request.POST.get('ingredients')
        instructions = request.POST.get('instructions')

        re = Food_Items(
            name = name,
            description = description,
            ingredients = ingredients,
            instructions = instructions
        )
        re.save()

    return redirect('food_item')

def EDIT_food_item(request):
    re = Food_Items.objects.all()
    context = {
        're' : re,
    }
    
    return redirect(request, 'food_item.html', context)

def UPDATE_food_item(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        ingredients = request.POST.get('ingredients')
        instructions = request.POST.get('instructions')

        re = Food_Items(
            id = id,
            name = name,
            description = description,
            ingredients = ingredients,
            instructions = instructions
        )
        re.save()
    return redirect('food_item')

def DELETE_food_item(request, id):
    re = Food_Items.objects.filter(id = id)
    re.delete()

    context = {
        're' : re,
    }

    return redirect('food_item')


def waste_type(request):
    ma = Waste_Types.objects.all()
    context = {
        'ma' : ma,
    }
    return render(request, 'waste_type.html', context)

def ADD_waste_type(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        ingredients = request.POST.get('ingredients')
        restaurant = request.POST.get('restaurant')

        ma = Waste_Types(
            name = name,
            description = description,
            ingredients = ingredients,
            restaurant = restaurant
        )
        ma.save()

    return redirect('waste_type')



def EDIT_waste_type(request):
    ma = Waste_Types.objects.all()
    context = {
        'ma' : ma,
    }
    
    return redirect(request, 'waste_type.html', context)

def UPDATE_waste_type(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        ingredients = request.POST.get('ingredients')
        restaurant = request.POST.get('restaurant')

        ma = Waste_Types(
            id = id,
            name = name,
            description = description,
            ingredients = ingredients,
            restaurant = restaurant
        )
        ma.save()
    return redirect('waste_type')

def DELETE_waste_type(request, id):
    ma = get_object_or_404(Waste_Types, id=id)
    ma.items.clear() 
    ma.delete()

    return redirect('waste_type')