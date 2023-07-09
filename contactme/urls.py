from django.urls import path
from . import views

urlpatterns = [
    path('', views.contactme, name='contactme'),
    path('thank_you/', views.thank_you, name='thank_you'),
]
