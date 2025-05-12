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
    - mensagem: string - mensagem de sucesso de registro
    - erro: string - mensagem de erro de registro
    """
    nome = request.data.get('nome')
    senha = request.data.get('senha')
    confirmacao_senha = request.data.get('confirmacaoSenha')
    email = request.data.get('email')

    if not nome or not senha:
        return Response({'erro': 'Nome e senha são obrigatórios.'}, status=400)
    
    if senha != confirmacao_senha:
        return Response({'erro': 'Senha e confirmação da senha devem ser iguais'}, status=400)

    try:
        user = User.objects.create_user(username=nome, password=senha, email=email)
        login(request, user)
        return Response({'messagem': 'Usuário criado com sucesso.'}, status=201)
    except Exception as e:
        return Response({'erro': str(e)}, status=401)
    

@csrf_exempt
@api_view(['POST'])
def login_usuario(request):
    """
    Faz login de um usuário
    
    campos:
    - nome: string (obrigatório)
    - senha: string (obrigatório)
    
    retorno:
    - mensagem: string - mensagem de sucesso de login
    - erro: string - mensagem de erro de login
    """
    nome = request.data.get('nome')
    senha = request.data.get('senha')

    usuario = authenticate(request, username=nome, password=senha)

    if usuario is not None:
        login(request, usuario)
        return Response({'messagem': 'Login realizado com sucesso.'}, status=201)
    else:
        return Response({'erro': 'Nome e/ou senha incorreto(s)'}, status=401)
    

@csrf_exempt
# faz com que essa rota apenas pode ser acessada por usuários que realizaram login
@login_required
@api_view(['GET'])
def logout_usuario(request):
    """
    Faz logout do usuário atual

    retorno:
    - mensagem: string - mensagem de sucesso de logout
    """
    logout(request)
    return Response({'messagem': 'Logout realizado com sucesso.'}, status=201)


@csrf_exempt
@login_required
@api_view(['PATCH'])
def editar_usuario(request):
    """
    Edita os dados de cadastro do usuário atual
    
    campos:
    - novoNome: string (opcional)
    - novaSenha: string (opcional)
    - novoEmail: string (opcional)
    
    retorno:
    - mensagem: string - mensagem de sucesso de edição
    - usuario: json - novos dados de cadastro do usuário
    """
    usuario = request.user
    novo_nome = request.data.get('novoNome')
    nova_senha = request.data.get('novaSenha')
    novo_email = request.data.get('novoEmail')
    
    if novo_nome:
        usuario.username = novo_nome
    if nova_senha:
        usuario.password = nova_senha
    if novo_email:
        usuario.email = novo_email
        
    usuario.save()
    
    return Response({'mensagem': 'usuario editado com sucesso', 'usuario': UserSerializer(usuario).data}, status=200)


@csrf_exempt
@login_required
@api_view(['DELETE'])
def deletar_usuario(request):
    """
    Deleta o usuário atual

    retorno:
    - mensagem: string - mensagem de sucesso de deleção
    """
    usuario = request.user
    logout(request)
    usuario.delete()
    return Response({'mensagem': 'usuario deletado com sucesso'}, status=200)


@csrf_exempt
@login_required
@api_view(['GET'])
def perfil_usuario(request):
    """
    Retorna todos os dados do usuário logado atualmente
    """
    usuario = request.user
    serializer = UserSerializer(usuario)
    return Response(serializer.data)
    