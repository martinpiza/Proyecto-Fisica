from django.urls import path
from .views import index, movimiento_circular, fuerza, leyes_newton, inicio

urlpatterns = [
    path('/', index, name='index'),
    path('', inicio, name='inicio'),
    path('movimiento-circular/', movimiento_circular, name='movimiento_circular'),
    path('fuerza/', fuerza, name='fuerza'),
    path('leyes-newton/', leyes_newton, name='leyes_newton'),
]
