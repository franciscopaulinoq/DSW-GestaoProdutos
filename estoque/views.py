from django.shortcuts import render
from .models import Categoria, Fornecedor, Produto

# Create your views here.

def ProdutosView(request):
    produtos = Produto.objects.all()
    context = {'produtos': produtos}
    return render(request, "produtos.html", context)

def CategoriasView(request):
    categorias = Categoria.objects.all()
    context = {'categorias': categorias}
    return render(request, "categorias.html", context)

def FornecedoresView(request):
    fornecedores = Fornecedor.objects.all()
    context = {'fornecedores': fornecedores}
    return render(request, "fornecedores.html", context)