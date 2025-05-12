from rest_framework import serializers
from .models import User


# Como o objeto Response da REST Framework não é capaz de renderizar objetos de modelo, temos
# que criar classes auxiliares chamadas "serializers" que convertem-os para dicionários
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        # define qual modelo vai ser lido
        model = User
        # define os campos do modelo a serem incluidos no dicionário
        # (pode ser uma lista com os nomes dos campos também mas aqui serão todos)
        fields = '__all__'