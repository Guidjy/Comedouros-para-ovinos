from django.urls import path
from . import views


# aqui definimos as rotas para nossas views
urlpatterns = [
    path('', views.exemplo_rota_api),
    path('todos_ovinos/', views.get_todos_ovinos),
    path('cadastrar_ovino/', views.cadastrar_ovino),
]
