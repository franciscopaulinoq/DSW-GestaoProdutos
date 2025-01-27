from .categorias import categoria_list, categoria_create
from .fornecedores import fornecedor_list, fornecedor_create
from .produtos import produto_list, produto_create, produto_detail

__all__ = [
    'categoria_list',
    'categoria_create',
    'fornecedor_list',
    'fornecedor_create',
    'produto_list',
    'produto_create',
    'produto_detail',
]