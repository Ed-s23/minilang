from django.urls import path
from . import views

urlpatterns = [
    path('', views.web_index, name='web_index'),
    path('run/', views.run_minilang, name='run_minilang'),
]
