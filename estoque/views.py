from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from django.urls import reverse
from .models import Categoria, Fornecedor, Produto
from .forms import ProdutoForm

# Create your views here.

def ProdutosView(request):
    produtos = Produto.objects.all()
    context = {'produtos': produtos}
    return render(request, "produtos.html", context)

def ProdutoDetailsView(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    context = {'produto': produto}
    return render(request, "produto-details.html", context)

def ProdutosAddView(request):
    if request.method == "POST":
        form = ProdutoForm(request.POST)
        if form.is_valid():
            produto = Produto()
            produto.nome = form.cleaned_data['nome']
            produto.codigo = form.cleaned_data['codigo']
            produto.descricao = form.cleaned_data['descricao']
            produto.preco = form.cleaned_data['preco']
            produto.quantidade_estoque = form.cleaned_data['quantidade_estoque']
            produto.fornecedor = form.cleaned_data['fornecedor']
            produto.save()
            produto.categorias.set(form.cleaned_data['categorias'])
            return HttpResponseRedirect(reverse('produtos'))
    else:
        form = ProdutoForm()
    
    return render(request, 'produto-add.html', {'form': form})

def CategoriasView(request):
    categorias = Categoria.objects.all()
    context = {'categorias': categorias}
    return render(request, "categorias.html", context)

def FornecedoresView(request):
    fornecedores = Fornecedor.objects.all()
    context = {'fornecedores': fornecedores}
    return render(request, "fornecedores.html", context)