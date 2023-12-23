from django.urls import path
from . import views

urlpatterns = [
    path('personajes/index', views.p_lista, name='p_lista'),
    path('personajes/lista', views.p_lista, name='p_lista'),
    path('personajes/ficha/', views.p_ficha, name='p_ficha'),
    path('personajes/del', views.p_delete, name='p_delete'),
    path('personajes/add', views.p_add, name='p_add'),
    path('personajes/search', views.p_search, name='p_search'),
    path('personajes/update', views.p_update, name='p_update'),
    path('', views.index, name='index'),

    path('series/index', views.s_lista, name='s_lista'),
    path('series/lista', views.s_lista, name='s_lista'),
    path('series/ficha/', views.s_ficha, name='s_ficha'),
    path('series/del', views.s_delete, name='s_delete'),
    path('series/add', views.s_add, name='s_add'),
    path('series/search', views.s_search, name='s_search'),
    path('series/update', views.s_update, name='s_update'),

    path('', views.index, name='index'),
]