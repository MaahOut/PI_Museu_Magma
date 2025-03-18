from django.contrib import admin
from .models import Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque', 'data_criacao')  # Adicione 'estoque' aqui
    search_fields = ('nome', 'descricao')
    list_filter = ('data_criacao',)