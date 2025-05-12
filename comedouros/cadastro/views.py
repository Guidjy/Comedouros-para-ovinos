from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User
from .serializers import UserSerializer


# Aqui criamos nossas views (funções que são rodadas quando uma rota definida em urls.py é acessada)


# faz com que essa view não requere autenticação csrf
@csrf_exempt
# define os métodos de requisição permitidos para essa view
@api_view(['GET'])
def exemplo_rota_api(request):
    # Retorna um objeto Response que renderiza o dicionário que passamos como JSON
    return Response({'mensagem': 'REST Framework funcionando!'})


@csrf_exempt
@api_view(['POST'])
def registrar_usuario(request):
    """
    Registra e faz login de um novo usuário
    
    campos:
    - nome: string (obrigatório)
    - senha: string (obrigatório)
    - confirmacaoSenha: string (obrigatório)
    - email: string (obrigatório)
    
    retorno:
    - mensagem: string - mensagem de erro ou sucesso de registro
    """
    # pega os dados passados no JSON da requisição
    nome = request.data.get('nome')
    senha = request.data.get('senha')
    confirmacao_senha = request.data.get('confirmacaoSenha')
    email = request.data.get('email')

    # verifica se os dados passados pelo usuário são válidos
    if not nome or not senha:
        return Response({'mensagem': 'Nome e senha são obrigatórios.'}, status=400)
    
    if senha != confirmacao_senha:
        return Response({'mensagem': 'Senha e confirmação da senha devem ser iguais'}, status=400)

    # tenta fazer o registro e login do usuário
    try:
        user = User.objects.create_user(username=nome, password=senha, email=email)
        login(request, user)
        return Response({'messagem': 'Usuário criado com sucesso.'}, status=201)
    except Exception as e:
        return Response({'mensagem': str(e)}, status=401)


@csrf_exempt
@api_view(['GET'])
def perfil(request):
    """
    Retorna todos os dados do usuário logado atualmente
    """
    usuario = request.user
    serializer = UserSerializer(usuario)
    return Response(serializer.data)
    