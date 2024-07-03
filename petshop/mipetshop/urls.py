from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('alimento-seco-gato/', views.alimento_seco_gato, name='alimento_seco_gato'),
    path('alimento-humedo-gato/', views.alimento_humedo_gato, name='alimento_humedo_gato'),
    path('alimento-perro/', views.alimento_perro, name='alimento_perro'),
    path('accesorios/', views.accesorios, name='accesorios'),
    path('api/', views.api, name='api'),
]