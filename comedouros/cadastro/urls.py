from django.urls import path
from . import views


# aqui definimos as rotas para nossas views
urlpatterns = [
    # Crud de usuário
    path('registrar_usuario/', views.registrar_usuario),
    path('login/', views.login_usuario),
    path('logout/', views.logout_usuario),
    path('editar_usuario/', views.editar_usuario),
    path('deletar_usuario/', views.deletar_usuario),
    path('perfil_usuario/', views.perfil_usuario),
]
