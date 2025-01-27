from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from estoque.models import Fornecedor
from estoque.forms import  FornecedorForm

def fornecedor_list(request):
    fornecedores = Fornecedor.objects.all()

    context = {
        'fornecedores': fornecedores
    }

    return render(request, "fornecedor.html", context)

def fornecedor_create(request):
    if request.method == "POST":
        form = FornecedorForm(request.POST)
        if form.is_valid():
            fornecedor = Fornecedor()
            fornecedor.nome = form.cleaned_data['nome']
            fornecedor.cnpj = form.cleaned_data['cnpj']
            fornecedor.telefone = form.cleaned_data['telefone']
            fornecedor.email = form.cleaned_data['email']
            fornecedor.save()
            return HttpResponseRedirect(reverse('fornecedores'))
    else:
        form = FornecedorForm()
    
    context = {
        'form': form
    }

    return render(request, 'fornecedor-create.html', context)