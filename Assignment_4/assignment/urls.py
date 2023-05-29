"""
URL configuration for assignment project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('', views.home, name='home'),
    path('Food_waste/', views.Food_waste, name='Food_waste'),
    path('app/', views.app, name='app'),
    path('add', views.ADD, name='add'),
    path('edit', views.EDIT, name='edit'), 
    path('update/<str:id>', views.UPDATE, name='update'), 
    path('delete/<str:id>', views.DELETE, name='delete'), 
    path('food_item/', views.food_item, name='food_item'),
    path('add_food_item', views.ADD_food_item, name='add_food_item'),
    path('edit_food_item', views.EDIT_food_item, name='edit_food_item'),
    path('update_food_item/<str:id>', views.UPDATE_food_item, name='update_food_item'), 
    path('delete_food_item/<str:id>', views.DELETE_food_item, name='delete_food_item'), 
    path('waste_type/', views.waste_type, name='waste_type'),
    path('add_waste_type', views.ADD_waste_type, name='add_waste_type'),
    path('edit_waste_type', views.EDIT_waste_type, name='edit_waste_type'),
    path('update_waste_type/<str:id>', views.UPDATE_waste_type, name='update_waste_type'), 
    path('delete_waste_type/<str:id>', views.DELETE_waste_type, name='delete_waste_type'),
]
