from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView
from estoque.models import Categoria, Fornecedor, Produto
from estoque.forms import  ProdutoForm

class ProdutoListView(ListView):
    model = Produto
    template_name = "produto.html"
    context_object_name = 'produtos'

class ProdutoCreateView(CreateView):
    model = Produto
    form_class = ProdutoForm
    template_name = "produto-create.html"
    success_url = reverse_lazy('produtos')

    def form_valid(self, form):
        response = super().form_valid(form)

        self.object.categorias.set(form.cleaned_data['categorias'])

        return response
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categorias"] = Categoria.objects.all()
        context["fornecedores"] = Fornecedor.objects.all()

        return context

class ProdutoDetailView(DetailView):
    model = Produto
    template_name = "produto-detail.html"
    context_object_name = "produto"

    def get_object(self, queryset=None):
        return get_object_or_404(Produto, id=self.kwargs["produto_id"])