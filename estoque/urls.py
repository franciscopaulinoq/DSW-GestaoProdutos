from django.urls import path
from .views import ProdutosView, CategoriasView, FornecedoresView

urlpatterns = [
    path('produtos/', ProdutosView, name="produtos"),
    path('categorias/', CategoriasView, name="categorias"),
    path('fornecedores/', FornecedoresView, name="fornecedores"),
]