from django.contrib import admin
from .models import Lote, Ovino, Refeicao

# Register your models here.
admin.site.register(Lote)
admin.site.register(Ovino)
admin.site.register(Refeicao)