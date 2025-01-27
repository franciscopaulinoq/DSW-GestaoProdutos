from django.urls import path
from .views import ProdutosView, ProdutoDetailsView, CategoriasView, FornecedoresView, ProdutosAddView, CategoriaAddView, FornecedorAddView

urlpatterns = [
    path('produtos/', ProdutosView, name="produtos"),
    path('produto/add/', ProdutosAddView, name='produto-add'),
    path('produto/<int:produto_id>', ProdutoDetailsView, name="produto-details"),
    path('categorias/', CategoriasView, name="categorias"),
    path('categoria/add/', CategoriaAddView, name='categoria-add'),
    path('fornecedores/', FornecedoresView, name="fornecedores"),
    path('fornecedor/add/', FornecedorAddView, name='fornecedor-add'),
]