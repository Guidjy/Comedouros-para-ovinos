from django.db import models
from django.contrib.auth.models import AbstractUser


# Criamos nossos modelos aqui. Podemos pensar neles como tabelas de um banco de dados
class User(AbstractUser):
    
    def __str__(self):
        return self.username
