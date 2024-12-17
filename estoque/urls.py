from django.urls import path
from .views import ProdutosView, ProdutoDetailsView, CategoriasView, FornecedoresView

urlpatterns = [
    path('produtos/', ProdutosView, name="produtos"),
    path('produto/<int:produto_id>', ProdutoDetailsView, name="produto-details"),
    path('categorias/', CategoriasView, name="categorias"),
    path('fornecedores/', FornecedoresView, name="fornecedores"),
]