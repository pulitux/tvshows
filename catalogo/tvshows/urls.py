from django.urls import path
from . import views

urlpatterns = [
    path('personajes/index', views.p_lista, name='p_lista'),
    path('personajes/lista', views.p_lista, name='p_lista'),
    path('personajes/ficha/', views.p_ficha, name='p_ficha'),
    path('personajes/del/', views.p_delete, name='p_delete'),
    path('personajes/add', views.p_add, name='p_add'),
    path('personajes/search', views.p_search, name='p_search'),
    path('', views.index, name='index'),
]