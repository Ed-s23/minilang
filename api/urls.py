# api/urls.py
#from django.urls import path
#from . import views

#urlpatterns = [
#    path('', views.index, name='index'),
#]

from django.urls import path
from .views import run_minilang

urlpatterns = [
    path('run/', run_minilang, name='run_minilang'),
]
