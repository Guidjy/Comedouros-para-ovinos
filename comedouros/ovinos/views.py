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
    
    id_brinco = request.data.get('idBrinco')
    nome = request.data.get('nome')
    peso = request.data.get('peso')
    idade_dias = request.data.get('idadeDias')
    foto = request.data.get('foto')
    lote = request.data.get('lote')
    consumo_diario = request.data.get('consumoDiario')
    custo_diario_racao = request.data.get('custoDiarioRacao')
    alimentacao_frequencia_livre = request.data.get('alimentacaoFrequenciaLivre')
    
    if not id_brinco and not nome:
        return Response({'erro': 'Providêncie pelomenos o id do brinco ou o nome do animal.'}, status=400)
    
    ovino = Ovino.objects.create(
        id_brinco=id_brinco,
        nome=nome,
        peso=peso,
        idade_dias=idade_dias,
        foto=foto,
        lote=lote,
        consumo_diario=consumo_diario,
        custo_diario_racao=custo_diario_racao,
        alimentacao_frequencia_livre=alimentacao_frequencia_livre
    )
    
    try:
        ovino.full_clean()
    except ValidationError as e:
        return Response({'erro': 'Campos do formulário inválidos.', 'mensagem': e}, status=400)
    else:
        serializer = OvinoSerializer(ovino)
        return Response({'sucesso': 'Animal cadastrado com sucesso.', 'ovino': serializer.data}, status=200)
    