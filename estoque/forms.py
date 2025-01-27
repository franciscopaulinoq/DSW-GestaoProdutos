from django import forms
from .models import Categoria, Fornecedor

class ProdutoForm(forms.Form):
    nome = forms.CharField(max_length=250, label="Nome")
    codigo = forms.CharField(max_length=15, label="Código")
    descricao = forms.CharField(widget=forms.Textarea, label="Descrição")
    preco = forms.DecimalField(max_digits=10, decimal_places=2, label="Preço")
    quantidade_estoque = forms.IntegerField(label="Quantidade em Estoque")
    categorias = forms.ModelMultipleChoiceField(
        queryset=Categoria.objects.all(), 
        widget=forms.CheckboxSelectMultiple, 
        label="Categorias")
    fornecedor = forms.ModelChoiceField(
        queryset=Fornecedor.objects.all(), 
        label="Fornecedor")

class CategoriaForm(forms.Form):
    nome = forms.CharField(max_length=250, label="Nome")

class FornecedorForm(forms.Form):
    nome = forms.CharField(max_length=250, label="Nome")
    cnpj = forms.CharField(max_length=14, label="CNPJ")
    telefone = forms.CharField(max_length=11, label="Telefone")
    email = forms.EmailField(max_length=254)