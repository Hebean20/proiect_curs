from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('modifica/<int:disponibitate>', views.disponibilitate, name='disponibilitate'),
    path('home/', views.home, name='home'),

    ]
