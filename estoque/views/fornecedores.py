from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView
from estoque.models import Fornecedor
from estoque.forms import  FornecedorForm

class FornecedorListView(ListView):
    model = Fornecedor
    template_name = "fornecedor.html"
    context_object_name = 'fornecedores'

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