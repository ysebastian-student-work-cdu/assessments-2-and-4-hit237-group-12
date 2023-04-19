from django.shortcuts import render
from .models import Item

# Create your views here.

def app(request):
    return render(request, 'myapp/app.html')

def home(request):
    return render(request, 'myapp/home.html')

def lists(request):
    return render(request, 'myapp/lists.html')

def details(request):
    return render(request, 'myapp/details.html')

def data_models(request):
    item1 = Item('Composting Bin', 'A bin designed for composting food scraps and other organic waste, reducing the amount of waste that ends up in landfills.')
    item2 = Item('Food Waste Tracker', 'A mobile app that helps users track and reduce their food waste by providing tips on how to store food properly and use up leftovers.')
    item3 = Item('Community Fridge', 'A public fridge where people can donate surplus food and others can take what they need, reducing food waste and helping those in need.')
    item4 = Item('Food Storage Containers', 'A set of reusable containers that help keep food fresh for longer and reduce the need for disposable packaging.')
    item5 = Item('Cooking Classes', 'Classes that teach people how to use up leftover ingredients and make the most of what they have in their fridge and pantry, reducing food waste and saving money.')
    item6 = Item('Food Donation Network', 'An online platform that connects food businesses with charities and non-profits to donate surplus food, reducing waste and helping those in need.')
    item7 = Item('Food Sharing Platform', 'A platform where individuals can share surplus food with others in their community, reducing waste and building stronger community connections.')
    item8 = Item('Food Rescue Program', 'A program that collects and redistributes food that would otherwise go to waste from grocery stores, restaurants, and other food businesses, reducing waste and providing food for those in need.')
    item9 = Item('Food Recovery App', 'An app that helps food businesses manage and redistribute surplus food, reducing waste and maximizing the use of resources.')

    item_list = [item1, item2, item3, item4, item5, item6, item7, item8, item9]
    context = {'item_list': item_list}
    return render(request, 'myapp/frontend.html', context)
