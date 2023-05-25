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
    path('operation/', views.operation, name='operation'),
    path('app/', views.app, name='app'),
    path('add', views.ADD, name='add'),
    path('edit', views.EDIT, name='edit'), 
    path('update/<str:id>', views.UPDATE, name='update'), 
    path('delete/<str:id>', views.DELETE, name='delete'), 
    path('recipe/', views.recipe, name='recipe'),
    path('add_recipe', views.ADD_recipe, name='add_recipe'),
    path('edit_recipe', views.EDIT_recipe, name='edit_recipe'),
    path('update_recipe/<str:id>', views.UPDATE_recipe, name='update_recipe'), 
    path('delete_recipe/<str:id>', views.DELETE_recipe, name='delete_recipe'), 
    path('manu/', views.manu, name='manu'),
    path('add_manu', views.ADD_manu, name='add_manu'),
    path('edit_manu', views.EDIT_manu, name='edit_manu'),
    path('update_manu/<str:id>', views.UPDATE_manu, name='update_manu'), 
    path('delete_manu/<str:id>', views.DELETE_manu, name='delete_manu'),
]
