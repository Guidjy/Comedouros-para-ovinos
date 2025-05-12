from django.contrib import admin
from .models import User


# Aqui registramos nossos modelos para que suas migrações possam ser aplicadas e sejam visíveis na interface admin
admin.site.register(User)
