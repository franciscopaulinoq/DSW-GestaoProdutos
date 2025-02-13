from .categorias import CategoriaCreateView, CategoriaListView
from .fornecedores import FornecedorCreateView, FornecedorListView
from .produtos import ProdutoCreateView, ProdutoDetailView, ProdutoListView
from .user import LoginPageView, RegisterView

__all__ = [
    'CategoriaCreateView',
    'CategoriaListView',
    'FornecedorCreateView',
    'FornecedorListView',
    'ProdutoCreateView',
    'ProdutoDetailView',
    'ProdutoListView',
    'LoginPageView',
    'RegisterView',
]