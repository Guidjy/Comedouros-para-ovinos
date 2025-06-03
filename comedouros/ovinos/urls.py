from django.urls import path
from . import views


# aqui definimos as rotas para nossas views
urlpatterns = [
    path('', views.exemplo_rota_api),
    path('get_ovino/<int:id>/', views.get_ovino),
    path('todos_ovinos/', views.get_todos_ovinos),
    path('cadastrar_ovino/', views.cadastrar_ovino),
    path('editar_ovino/', views.editar_ovino),
    path('deletar_ovino/<int:id>/', views.deletar_ovino),
]
