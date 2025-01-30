from django.urls import path
from .views import *

urlpatterns = [
    path('produtos/', ProdutoListView.as_view(), name="produtos"),
    path('produto/add/', produto_create, name='produto-create'),
    path('produto/<int:produto_id>', produto_detail, name="produto-detail"),
    path('categorias/', CategoriaListView.as_view(), name="categorias"),
    path('categoria/add/', categoria_create, name='categoria-create'),
    path('fornecedores/', FornecedorListView.as_view(), name="fornecedores"),
    path('fornecedor/add/', fornecedor_create, name='fornecedor-create'),
]