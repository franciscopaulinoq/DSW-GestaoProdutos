from django.contrib import admin
from estoque.models import *

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome']

class FornecedorAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cnpj', 'telefone', 'email']    

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'codigo', 'data_criacao', 'preco', 'quantidade_estoque']
    search_fields = ['nome', 'codigo']
    list_filter = ['data_criacao']
    ordering = ['-data_criacao']

admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Fornecedor, FornecedorAdmin)