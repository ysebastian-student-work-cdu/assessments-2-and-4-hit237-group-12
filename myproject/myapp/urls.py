from . import views
from django.urls import include, path
urlpatterns = [
    path('app/', views.app, name='app'),
]
