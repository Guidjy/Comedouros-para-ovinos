from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.exceptions import ValidationError
from .models import Ovino
from .serializers import OvinoSerializer


# define os métodos de requisição permitidos para essa view
@api_view(['GET'])
def exemplo_rota_api(request):
    # Retorna um objeto Response que renderiza o dicionário que passamos como JSON
    return Response({'mensagem': 'REST Framework funcionando!'})


@api_view(['GET'])
def get_ovino(request, id):
    """
    Retorna os dados do ovino de id "id"
    
    retorno:
    - ovino: json com os dados
    """
    try:
        ovino = Ovino.objects.get(id=id)
    except Ovino.DoesNotExist:
        return Response({'erro': 'Não existe um animal com esse id.'}, status=400)
    
    serializer = OvinoSerializer(ovino)
    return Response(serializer.data, status=200)


@api_view(['GET'])
def get_todos_ovinos(request):
    """
    Lista todos os ovinos registrados
    
    retorno:
    - ovinos: lista com os dados dos ovinos
    """
    ovinos = Ovino.objects.all()
    serializer = OvinoSerializer(ovinos, many=True)
    return Response({'ovinos': serializer.data})


@api_view(['POST'])
def cadastrar_ovino(request):
    """
    Cadastra um novo ovino
    
    campos:
    - idBrinco: int 
    - nome: string
    obs: pelomenos ou idBrinco ou nome deve ser providêciado
    - peso: float (opcional)
    - idadeDias: int (opcional)
    - foto: arquivo (opcional)
    - lote: int (id do lote) (opcional)
    - consumoDiario: float (opcional)
    - custoDiarioRacao: float (opcional)
    - alimentacaoFrequenciaLivre: bool (opcional)
    
    retorno:
    - sucesso: mensagem de sucesso (condicional)
    - erro: mensagem de erro (condicional)
    - ovino: dados do ovino criado
    """
    
    data = request.data
    
    if not data.get('idBrinco') and not data.get('nome'):
        return Response({'erro': 'Providêncie pelo menos o id do brinco ou o nome do animal.'}, status=400)

    ovino = Ovino(
        id_brinco=data.get('idBrinco'),
        nome=data.get('nome'),
        peso=data.get('peso'),
        idade_dias=data.get('idadeDias'),
        foto=data.get('foto'),
        lote=data.get('lote'),
        consumo_diario=data.get('consumoDiario'),
        custo_diario_racao=data.get('custoDiarioRacao'),
        alimentacao_frequencia_livre=data.get('alimentacaoFrequenciaLivre'),
    )

    try:
        ovino.full_clean()
        ovino.save()
    except ValidationError as e:
        return Response({'erro': 'Campos do formulário inválidos.', 'mensagem': e.message_dict}, status=400)

    serializer = OvinoSerializer(ovino)
    return Response({'sucesso': 'Animal cadastrado com sucesso.', 'ovino': serializer.data}, status=200)
    

@api_view(['GET', 'PATCH'])  # GET APENAS PARA TESTAGEM
def editar_ovino(request):
    """
    atualiza os dados do ovino de um certo id
    
    campos:
    - id: int 
    - idBrinco: int (opcional)
    - nome: string (opcional)
    - peso: float (opcional)
    - idadeDias: int (opcional)
    - foto: arquivo (opcional)
    - lote: int (id do lote) (opcional)
    - consumoDiario: float (opcional)
    - custoDiarioRacao: float (opcional)
    - alimentacaoFrequenciaLivre: bool (opcional)
    
    retorno:
    - sucesso: mensagem de sucesso (condicional)
    - erro: mensagem de erro (condicional)
    - ovino: dados atualizados do ovino
    """
    
    ############### DELETAR DEPOIS
    if request.method == 'GET':
        return Response({'mensagem': 'Use PATCH para editar dados.'})
    ###############
    
    data = request.data
    
    if not data.get('id'):
        return Response({'erro': 'Proviêcie o id do animal (obs: não id de tag)'}, status=400)
    
    try:
        ovino = Ovino.objects.get(id=data.get('id'))
    except Ovino.DoesNotExist:
        return Response({'erro': 'Não existe um animal com esse id.'}, status=400)
    
    campos_atualizaveis = {
        'idBrinco': 'id_brinco',
        'nome': 'nome',
        'peso': 'peso',
        'idadeDias': 'idade_dias',
        'foto': 'foto',
        'lote': 'lote',
        'consumoDiario': 'consumo_diario',
        'custoDiarioRacao': 'custo_diario_racao',
        'alimentacaoFrequenciaLivre': 'alimentacao_frequencia_livre',
    }
    
    for chave_request, campo_model in campos_atualizaveis.items():
        if chave_request in data:
            # https://www.w3schools.com/python/ref_func_setattr.asp
            setattr(ovino, campo_model, data.get(chave_request))
            
    try:
        ovino.full_clean()
        ovino.save()
    except ValidationError as e:
        return Response({'erro': 'Campos inválidos.', 'mensagem': e.message_dict}, status=400)
    
    sereializer = OvinoSerializer(ovino)
    return Response({'successo': 'Animal editado com sucesso.', 'ovino': sereializer.data}, status=200)


@api_view(['DELETE'])
def deletar_ovino(request, id):
    """
    deleta o ovino de id "id"
    
    retorno:
    - sucesso: mensagem de sucesso (condicional)
    - erro: mensagem de erro (condicional)
    """
    
    try:
        ovino = Ovino.objects.get(id=id)
    except Ovino.DoesNotExist:
        return Response({'erro': 'Não existe um animal com esse id.'}, status=400)
    
    ovino.delete()
    return Response({'sucesso': 'Animal deletado com sucesso.'}, status=200)
    
    