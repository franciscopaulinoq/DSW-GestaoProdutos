from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from estoque.models import Categoria
from estoque.forms import  CategoriaForm

class CategoriaListView(LoginRequiredMixin, ListView):
    model = Categoria
    template_name = "categoria.html"
    context_object_name = 'categorias'

class CategoriaCreateView(LoginRequiredMixin, CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = "categoria-create.html"
    success_url = reverse_lazy('categorias')