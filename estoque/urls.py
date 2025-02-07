from django.urls import path
from .views import *

urlpatterns = [
    path('produtos/', ProdutoListView.as_view(), name="produtos"),
    path('produtos/page/<int:page>/', ProdutoListView.as_view(), name='produtos-list-paginated'),
    path('produto/add/', ProdutoCreateView.as_view(), name='produto-create'),
    path('produto/<int:produto_id>', ProdutoDetailView.as_view(), name="produto-detail"),
    path('categorias/', CategoriaListView.as_view(), name="categorias"),
    path('categoria/add/', CategoriaCreateView.as_view(), name='categoria-create'),
    path('fornecedores/', FornecedorListView.as_view(), name="fornecedores"),
    path('fornecedor/add/', FornecedorCreateView.as_view(), name='fornecedor-create'),
]