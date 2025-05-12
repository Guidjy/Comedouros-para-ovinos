from django.urls import path
from . import views


# aqui definimos as rotas para nossas views
urlpatterns = [
    path('', views.exemplo_rota_api),
    path('registrar/', views.registrar_usuario),
    path('perfil/', views.perfil),
]
