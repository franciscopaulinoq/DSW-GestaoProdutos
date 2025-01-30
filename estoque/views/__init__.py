from .categorias import categoria_list, categoria_create, CategoriaListView
from .fornecedores import fornecedor_list, fornecedor_create, FornecedorListView
from .produtos import produto_list, produto_create, produto_detail, ProdutoListView

__all__ = [
    'categoria_list',
    'categoria_create',
    'CategoriaListView',
    'fornecedor_list',
    'fornecedor_create',
    'FornecedorListView',
    'produto_list',
    'produto_create',
    'produto_detail',
    'ProdutoListView'
]