from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from estoque.models import Fornecedor
from estoque.forms import  FornecedorForm

class FornecedorListView(LoginRequiredMixin, ListView):
    model = Fornecedor
    template_name = "fornecedor.html"
    context_object_name = 'fornecedores'

class FornecedorCreateView(LoginRequiredMixin, CreateView):
    model = Fornecedor
    form_class = FornecedorForm
    template_name = "fornecedor-create.html"
    success_url = reverse_lazy('fornecedores')