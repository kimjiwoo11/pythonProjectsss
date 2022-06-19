from django.urls import path
from . import views

app_name = 'detail'

urlpatterns = [
    path('bott/', views.bott, name='bott'),

    path('to/', views.to, name='to'),
    path('out/', views.out, name='out'),
]