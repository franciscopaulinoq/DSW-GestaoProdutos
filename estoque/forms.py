from django import forms
from .models import Categoria, Fornecedor
import re

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

    def clean_cnpj(self):
        cnpj = self.cleaned_data.get('cnpj')
        if cnpj and not re.match(r'^\d{14}$', cnpj):
            raise forms.ValidationError("O CNPJ Deve Conter Apenas 14 Números.")
        return cnpj
    
    def clean_telefone(self):
        telefone = self.cleaned_data.get('telefone')
        if telefone and not re.match(r'^\d{10,11}$', telefone):
            raise forms.ValidationError("O Telefone Deve Conter Apenas Números, com 10 ou 11 Dígitos.")
        return telefone
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and not re.match(r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b$', email):
            raise forms.ValidationError("Digite um Endereço de E-mail Válido.")
        return email