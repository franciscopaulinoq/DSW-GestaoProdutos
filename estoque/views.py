from django.shortcuts import get_object_or_404, render
from .models import Categoria, Fornecedor, Produto

# Create your views here.

def ProdutosView(request):
    produtos = Produto.objects.all()
    context = {'produtos': produtos}
    return render(request, "produtos.html", context)

def ProdutoDetailsView(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    context = {'produto': produto}
    return render(request, "produto-details.html", context)

def CategoriasView(request):
    categorias = Categoria.objects.all()
    context = {'categorias': categorias}
    return render(request, "categorias.html", context)

def FornecedoresView(request):
    fornecedores = Fornecedor.objects.all()
    context = {'fornecedores': fornecedores}
    return render(request, "fornecedores.html", context)