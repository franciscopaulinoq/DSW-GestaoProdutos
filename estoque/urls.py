from django.urls import path
from .views import *

urlpatterns = [
    path('produtos/', produto_list, name="produtos"),
    path('produto/add/', produto_create, name='produto-add'),
    path('produto/<int:produto_id>', produto_detail, name="produto-detail"),
    path('categorias/', categoria_list, name="categorias"),
    path('categoria/add/', categoria_create, name='categoria-add'),
    path('fornecedores/', fornecedor_list, name="fornecedores"),
    path('fornecedor/add/', fornecedor_create, name='fornecedor-add'),
]