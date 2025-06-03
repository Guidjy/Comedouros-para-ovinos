from django.db import models


class Lote(models.Model):
    numero_de_animais = models.IntegerField(default=0)
    ultima_atualizacao = models.DateTimeField(auto_now=True)


class Ovino(models.Model):
    id_brinco = models.IntegerField(blank=True, null=True)
    nome = models.CharField(max_length=50, blank=True, null=True)
    peso = models.FloatField(blank=True, null=True)
    idade_dias = models.IntegerField(blank=True, null=True)
    foto = models.ImageField(blank=True, null=True)
    lote = models.ForeignKey(Lote, blank=True, null=True, on_delete=models.SET_NULL)
    consumo_diario = models.FloatField(blank=True, null=True)
    custo_diario_racao = models.FloatField(blank=True, null=True)
    alimentacao_frequencia_livre = models.BooleanField(blank=True, null=True)
    ultima_atualizacao = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.id_brinco}'
    

class Refeicao(models.Model):
    ovino = models.OneToOneField(Ovino, on_delete=models.CASCADE)
    dia = models.DateField()
    horario_entrada = models.TimeField(blank=True, null=True)
    peso_na_entrada = models.FloatField(blank=True, null=True)
    duracao_refeicao = models.DurationField(blank=True, null=True)
    peso_racao = models.FloatField(blank=True, null=True)
    variacao_peso = models.FloatField(blank=True, null=True)
    comportamento = models.TextField(default='', blank=True)
    ultima_atualizacao = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.ovino} comeu {self.consumo}g no dia {self.dia_horario}'
    
    
