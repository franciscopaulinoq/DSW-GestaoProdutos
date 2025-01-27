from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from django.urls import reverse
from estoque.models import Categoria, Fornecedor, Produto
from estoque.forms import  ProdutoForm

def produto_list(request):
    produtos = Produto.objects.all()

    context = {
        'produtos': produtos
    }
    
    return render(request, "produto.html", context)

def produto_create(request):
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
    
    categorias = Categoria.objects.all()
    fornecedores = Fornecedor.objects.all()
    
    context = {
        'form': form, 
        'categorias': categorias, 
        'fornecedores': fornecedores
    }
    
    return render(request, 'produto-create.html', context)

def produto_detail(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)

    context = {
        'produto': produto
    }

    return render(request, "produto-detail.html", context)