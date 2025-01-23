from django.urls import path
from .views import ProdutosView, ProdutoDetailsView, CategoriasView, FornecedoresView, ProdutosAddView

urlpatterns = [
    path('produtos/', ProdutosView, name="produtos"),
    path('produto/add/', ProdutosAddView, name='produto-add'),
    path('produto/<int:produto_id>', ProdutoDetailsView, name="produto-details"),
    path('categorias/', CategoriasView, name="categorias"),
    path('fornecedores/', FornecedoresView, name="fornecedores"),
]