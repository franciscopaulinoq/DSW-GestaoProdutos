from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from estoque.models import Categoria
from estoque.forms import  CategoriaForm

def categoria_list(request):
    categorias = Categoria.objects.all()

    context = {
        'categorias': categorias
    }

    return render(request, "categoria.html", context)

def categoria_create(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            categoria = Categoria()
            categoria.nome = form.cleaned_data['nome']
            categoria.save()
            return HttpResponseRedirect(reverse('categorias'))
    else:
        form = CategoriaForm()
    
    context = {
        'form': form
    }
    
    return render(request, 'categoria-create.html', context)